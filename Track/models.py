from django.db import models

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=100)
    rollnumber = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    phonenumber = models.IntegerField(unique=True)
    user_id = models.CharField(max_length=100,unique=True)
    set_password = models.CharField(max_length = 100)

    def __str__(self):
        return self.name 
    
class login(models.Model):
    user_id = models.ForeignKey(register, on_delete=models.CASCADE,related_name='login_user' )

    def __str__(self):
     return self.user.user_id