from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    rollnumber = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(unique=True)

    def __str__(self):
        return self.username
    
class Found(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )  #unique identifier
    rollnumber = models.IntegerField(null=True, blank=True)
    nameofarticle = models.CharField(max_length = 100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)



    def __str__(self):
        return self.nameofarticle


class Lost(models.Model):
    id = models.UUIDField(primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    rollnumber = models.IntegerField(null=True, blank=True)
    nameofarticle = models.CharField(max_length = 100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    resolved = models.BooleanField(default=False)

    found_name = models.OneToOneField(
        Found,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lost_item"
    )

    def __str__(self):
        return self.nameofarticle



