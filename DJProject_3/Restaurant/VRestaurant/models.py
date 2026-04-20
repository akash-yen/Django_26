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
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES, blank=True, null=True)
    always_available = models.BooleanField(
        default=False,
        help_text="If checked, this item appears on breakfast, lunch, and dinner menus.",
    )

    def __str__(self):
        if self.always_available:
            return f"{self.name} (All Day)"
        return f"{self.name} ({self.meal_type})"
