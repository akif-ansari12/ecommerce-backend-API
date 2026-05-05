from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHIOCES = (
        ('customer', 'customer'),
        ('seller', 'seller'),
        ('admin', 'admin'),
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHIOCES, default='buyer')