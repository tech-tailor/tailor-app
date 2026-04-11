# Tailor App

A full-featured Django-based e-commerce platform for a tailoring business. The application manages products, orders, customer measurements, and provides an online shopping experience for custom clothing.

## Overview

Tailor App is a web-based platform for a bespoke tailoring service. Customers can browse products, upload their measurements, and place orders for custom-made clothing.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Authentication**: Django Allauth with OpenID support

## Project Structure

```
tailor-app/
├── tailorApp/           # Main Django project
│   ├── settings.py    # Settings (dev/prod)
│   ├── urls.py       # URL routing
│   ├── views.py     # Core views
│   ├── wsgi.py      # WSGI config
│   ├── asgi.py      # ASGI config
│   └── hosts.py     # Multi-host configuration
├── store/             # Store app
│   ├── models.py     # Database models
│   ├── views.py     # Store views
│   ├── urls.py      # Store URLs
│   ├── forms.py    # Django forms
│   └── templates/   # HTML templates
├── templates/         # Shared templates
│   └── openid/      # OpenID templates
└── work/             # Work utilities
    └── decorators.py # Custom decorators
```

## Features

- User authentication (email/password, social login)
- Product catalog with categories and tags
- Product search and filtering
- Customer measurement management
- Shopping cart
- Order processing
- Profile management
- Admin dashboard

## Models

| Model | Description |
|-------|-------------|
| `Size` | Clothing sizes |
| `Category` | Product categories |
| `Tag` | Product tags |
| `Product` | Clothing products |
| `Measurement` | Customer measurements |
| `Order` | Customer orders |

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Usage

Access the application at `http://127.0.0.1:8000/`

- Browse products at `/store/`
- Upload measurements at `/store/upload-measurement/`
- Manage profile at `/store/myprofile/`
- Admin panel at `/admin/`

## Settings

Configuration files:
- `settings.py` - Base settings
- `settings_dev.py` - Development overrides
- `settings_prod.py` - Production overrides

## License

MIT License