from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    Phone_Number=models.CharField(max_length=15,null=False,blank=False)
    email=models.EmailField(null=False,blank=False)
# Create your models here.
