from django.contrib import admin
from .models import User,Lost,Found
# Register your models here.

admin.site.register(User)
admin.site.register(Lost)
admin.site.register(Found)