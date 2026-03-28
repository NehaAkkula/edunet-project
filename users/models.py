from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_homemaker = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class HomemakerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='homemaker_profile')
    delivery_radius = models.IntegerField(help_text="In kilometers", default=5)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Profile"
