# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django restaurant web application. The goal is to display a **time-based menu UI** — the menu shown to users changes automatically depending on the server's current time (breakfast in the morning, lunch in the afternoon, dinner in the evening). Menu data is managed via the database and updated through the Django admin.

## Project Layout

```
DJProject_3/
└── Restaurant/          # Django project root (contains manage.py)
    ├── manage.py
    ├── db.sqlite3
    ├── Restaurant/      # Django settings package
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── VRestaurant/     # Main Django app
        ├── models.py    # Menu models go here
        ├── views.py     # Time-based menu logic goes here
        ├── admin.py     # Register models for admin management
        └── migrations/
```

- Django version: 3.2.4
- Database: SQLite (`db.sqlite3`) — default, no additional setup needed
- `TIME_ZONE` is currently `'UTC'` in `settings.py` — adjust to the restaurant's local timezone when building the time-based logic

## Common Commands

All commands must be run from `Restaurant/` (where `manage.py` lives):

```bash
cd Restaurant

# Run the dev server
python manage.py runserver

# Create and apply migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Open Django shell (for quick DB queries)
python manage.py shell

# Create a superuser for the admin panel
python manage.py createsuperuser

# Run tests
python manage.py test VRestaurant

# Run a single test
python manage.py test VRestaurant.tests.TestClassName.test_method_name
```

## Architecture Plan: Time-Based Menu

The core feature works as follows:

1. **Models** (`VRestaurant/models.py`) — A `MenuItem` model with fields for name, description, price, image, and a `meal_type` choice field (`breakfast`, `lunch`, `dinner`).
2. **Views** (`VRestaurant/views.py`) — The view reads `datetime.now().hour` (using the server's local time), determines the current meal period, and filters `MenuItem.objects.filter(meal_type=current_meal)` to pass to the template.
3. **Templates** (`VRestaurant/templates/VRestaurant/`) — Django templates render the filtered menu items; use `APP_DIRS: True` (already set) so templates are discovered automatically.
4. **URLs** — Wire the home view in `Restaurant/urls.py` via `include('VRestaurant.urls')`.
5. **Admin** (`VRestaurant/admin.py`) — Register `MenuItem` so menu data can be managed without code changes.

### Meal time windows (suggested defaults, adjust as needed)
| Meal      | Hour range (server local time) |
|-----------|-------------------------------|
| Breakfast | 06:00 – 11:59                 |
| Lunch     | 12:00 – 16:59                 |
| Dinner    | 17:00 – 22:59                 |

> Remember to set `TIME_ZONE` in `settings.py` to the correct timezone (e.g., `'America/New_York'`) and keep `USE_TZ = True` so Django handles timezone conversion correctly.
