# Library Management System - Backend API 📚⚙️

This repository contains the **Backend API** for the **Library Management System**, designed to serve as a robust, headless engine managing books, clients, and active loans.

## 🔗 Live Application
- **Frontend Live Demo:** [Click Here to Visit](https://library-frontend-final.netlify.app/)  

## 🛠 Tech Stack
- **Framework:** Python 3, Django 5.x, Django REST Framework (DRF)
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **Authentication:** JWT (JSON Web Tokens) via `djangorestframework-simplejwt`
- **Server/Deployment:** Gunicorn, WhiteNoise (for static file serving)

---

## 🏗 System Architecture & Key Features

### 1. Fully-Fledged REST API
Implements complete **CRUD (Create, Read, Update, Delete)** architecture across the core domain models:
- **Books:** Inventory tracking and availability status.
- **Clients:** User management and registration.
- **Loans:** Transactional records binding clients to books, including due dates and return handling.

### 2. Secure JWT Authentication
- Uses short-lived Access Tokens and long-lived Refresh Tokens to ensure stateless, scalable, and secure API requests.
- Endpoints are protected with proper authorization guards, ensuring only authenticated users (e.g., `shaked_admin`) can modify inventory.

### 3. Production-Ready Configuration
- Configured with `dj-database-url` to dynamically parse database environment variables.
- Uses `django-cors-headers` to strictly manage Cross-Origin Resource Sharing with the designated frontend.
- Integrates `whitenoise` for optimized and completely self-contained static file serving (ideal for PaaS deployments like Render or Heroku).

---

## ⚙️ Running Locally
To run this backend server locally:

1. Clone the repository and navigate into the folder.
2. Create and activate a virtual environment:
   ```bash
   python -m virtualenv myenv
   # Windows: myenv\Scripts\activate
   # macOS/Linux: source myenv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations to initialize your local database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. *(Optional)* Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   
*Designed and Developed by [Shaked Liloz](https://github.com/shakedgoren)*
