from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class User_Accounts(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True,primary_key=True)
    password = models.CharField(max_length=100)

class EmailOtp(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    def is_expired(self):
        return timezone.now()> self.created_at+timedelta(minutes=3)  
