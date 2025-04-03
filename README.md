# UserAccount Django Project

This is a Django-based project for user authentication and account management. It includes features such as registration, login, logout, and user management.

## Features

- **User Registration**: Users can create an account with a username and password.
- **User Login**: Authenticated users can log in with their credentials.
- **User Logout**: Authenticated users can log out from the application.
- **Rate Limiting**: To prevent brute-force attacks, rate limiting is implemented for login attempts.
- **Custom User Model**: The project uses a custom user model for better flexibility in user management.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.12
- Django 4.2.2

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/WuorBhang/UserAccount.git

Navigate to the project directory:

bash

```bash
cd UserAccount
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On Mac/Linux:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Technologies Used

Django: The main web framework for the project.

Python: The programming language used for the project.

SQLite: The database used for development (can be changed in settings).

Git: Version control for managing the project.

## Contributing

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. """
