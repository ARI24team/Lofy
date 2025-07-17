from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    Phone_Number=models.CharField(max_length=15,null=False, blank=True)
    email=models.EmailField(null=False, blank=True)
    email_confirmed = models.BooleanField(default=True)
# Create your models here.
