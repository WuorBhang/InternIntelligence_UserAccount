from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.middleware.csrf import get_token
import json
from django_ratelimit.decorators import ratelimit
from .forms import RegisterForm, LoginForm

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = RegisterForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "User registered successfully"})
        return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = LoginForm(data)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({"message": "Login successful", "csrf_token": get_token(request)})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
        return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_protect
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logout successful"})
    return JsonResponse({"error": "Invalid request method"}, status=405)
