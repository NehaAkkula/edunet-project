from django.db import models
from django.conf import settings

class Order(models.Model):
    STATUS_CHOICES = [
        ('Ordered', 'Ordered'),
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Denied', 'Denied'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    dish = models.ForeignKey('dishes.Dish', on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Ordered')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.dish.name}"
