App Points Platform - Django Evaluation Project

Overview

This project is a Django-based web application that enables:
- Admins to manage Android app tasks and assign points.
- Users to view assigned tasks and upload screenshots upon task completion.

The project exposes a REST API with authentication and documentation.

---

Features

# Authentication
- Token-based authentication (via Djoser).
- Signup, login, profile management.

# Admin
- Add Android apps with description and point value.
- View and manage submitted user tasks.

# User
- View apps/tasks.
- View points earned.
- Track completed tasks.

# REST API
- All APIs exposed using Django REST Framework.
- Interactive API documentation via SwaggerI.

---

# Tech Stack

- Backend: Django, Django REST Framework
- Auth: Djoser + Token Auth
- Docs: drf-yasg (Swagger)
- Storage: SQLite (for development)
- File Upload: Media handling using Django's `ImageField`

---

# Getting Started

# Setup Locally

```bash
# Clone the repository
git clone https://gitlab.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
