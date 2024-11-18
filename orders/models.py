from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # For tracking who created the order
from MANAGER.models import Product  # Assuming Product is in inventory app

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to product
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically calculate total price based on product price and quantity
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
