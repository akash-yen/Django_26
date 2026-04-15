from django.contrib import admin
from .models import ZodiacSign, DailyPrediction


@admin.register(ZodiacSign)
class ZodiacSignAdmin(admin.ModelAdmin):
    list_display = ("name", "symbol", "element", "ruling_planet", "date_range")
    list_filter = ("element",)
    search_fields = ("name", "ruling_planet")


@admin.register(DailyPrediction)
class DailyPredictionAdmin(admin.ModelAdmin):
    list_display = ("zodiac_sign", "date", "lucky_number", "lucky_color", "created_at")
    list_filter = ("zodiac_sign", "date")
    search_fields = ("zodiac_sign__name",)
    ordering = ("-date",)
