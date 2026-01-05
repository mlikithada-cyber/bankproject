from django.db import models

# Create your models here.
class User_Accounts(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True,primary_key=True)
    password = models.CharField(max_length=100)

    
