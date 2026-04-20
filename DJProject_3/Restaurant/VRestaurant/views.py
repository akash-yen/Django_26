from django.shortcuts import render
from datetime import datetime
from .models import MenuItem


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
    meal_type = get_meal_type()
    menu_items = MenuItem.objects.filter(meal_type=meal_type) if meal_type else MenuItem.objects.none()
    return render(request, 'VRestaurant/home.html', {
        'menu_items': menu_items,
        'meal_type': meal_type,
    })
