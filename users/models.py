from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    rollnumber = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(unique=True)

    def __str__(self):
        return self.username

class Lost(models.Model):
    rollnumber = models.IntegerField(null=True, blank=True)
    nameofarticle = models.CharField(max_length = 100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    resolved = models.BooleanField(default=False)

class Found(models.Model):
    rollnumber = models.IntegerField(null=True, blank=True)
    nameofarticle = models.CharField(max_length = 100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)



