from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
