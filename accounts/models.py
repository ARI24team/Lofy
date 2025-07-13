from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    Phone_Number=models.CharField(max_length=15,null=False)
    email=models.EmailField(null=False)
# Create your models here.
