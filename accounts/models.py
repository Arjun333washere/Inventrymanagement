from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ('Admin', 'Admin'),
        ('Sales Staff', 'Sales Staff'),
        ('Manager', 'Manager')
    ])
    def save(self, *args, **kwargs):
        # Check if the role is 'Admin' and set is_superuser accordingly
        if self.is_superuser:
            self.role = 'Admin'
            
        super().save(*args, **kwargs)