from django.db import models


class ZodiacSign(models.Model):
    ELEMENT_CHOICES = [
        ("fire", "Fire"),
        ("earth", "Earth"),
        ("air", "Air"),
        ("water", "Water"),
    ]

    name = models.CharField(max_length=20, unique=True)
    symbol = models.CharField(max_length=10)
    element = models.CharField(max_length=10, choices=ELEMENT_CHOICES)
    ruling_planet = models.CharField(max_length=30)
    date_range = models.CharField(max_length=50, help_text="e.g. 'March 21 – April 19'")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DailyPrediction(models.Model):
    zodiac_sign = models.ForeignKey(
        ZodiacSign,
        on_delete=models.CASCADE,
        related_name="predictions",
    )
    date = models.DateField()
    love = models.TextField()
    career = models.TextField()
    health = models.TextField()
    overall = models.TextField()
    lucky_number = models.PositiveSmallIntegerField()
    lucky_color = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("zodiac_sign", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.zodiac_sign} — {self.date}"
