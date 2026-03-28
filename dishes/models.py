from django.db import models
from django.conf import settings
from django.db.models import Avg

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Meals', 'Meals'),
        ('Indian', 'Indian'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='dishes/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    homemaker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='dishes')

    @property
    def average_rating(self):
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0

    def __str__(self):
        return self.name
