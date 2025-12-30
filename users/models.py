from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime 
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('CUSTOMER','Customer'),
        ('STAFF','Staff'),
        ('MANAGER','Manager')
    )
    role = models.CharField(max_length=10,choices=ROLE_CHOICES)
    phone = models.CharField(max_length=10)
    kyc_verified = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.datetime.now())