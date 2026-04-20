from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal_type', 'always_available', 'price')
    list_filter = ('meal_type', 'always_available')
    search_fields = ('name', 'description')
