from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True,max_length=255)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
