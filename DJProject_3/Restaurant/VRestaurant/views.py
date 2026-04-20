from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from .models import MenuItem

MEAL_ORDER = ['breakfast', 'lunch', 'dinner']

MEALS = [
    {'type': 'breakfast', 'icon': '☕', 'hours': '6:00 AM – 11:59 AM'},
    {'type': 'lunch',     'icon': '🍛', 'hours': '12:00 PM – 4:59 PM'},
    {'type': 'dinner',    'icon': '🌙', 'hours': '5:00 PM – 10:59 PM'},
]


def get_meal_type():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        return 'breakfast'
    elif 12 <= hour < 17:
        return 'lunch'
    elif 17 <= hour < 23:
        return 'dinner'
    return None


def home(request):
    return render(request, 'VRestaurant/home.html', {
        'current_meal': get_meal_type(),
        'meals': MEALS,
    })


def menu(request, meal_type):
    if meal_type not in MEAL_ORDER:
        raise Http404("Unknown meal type")

    current_meal = get_meal_type()

    if meal_type == current_meal:
        menu_items = MenuItem.objects.filter(meal_type=meal_type)
        return render(request, 'VRestaurant/menu.html', {
            'menu_items': menu_items,
            'meal_type': meal_type,
            'current_meal': current_meal,
            'is_available': True,
        })

    if current_meal is None:
        message = "We are currently closed. Please visit us during our serving hours."
    elif MEAL_ORDER.index(meal_type) < MEAL_ORDER.index(current_meal):
        message = f"{meal_type.capitalize()} timing is done. Only {current_meal} can be provided now."
    else:
        message = f"{meal_type.capitalize()} timing hasn't started yet. Currently {current_meal} is being served."

    return render(request, 'VRestaurant/menu.html', {
        'meal_type': meal_type,
        'current_meal': current_meal,
        'is_available': False,
        'message': message,
    })
