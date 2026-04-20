from django.db import models


class MenuItem(models.Model):
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.meal_type})"
