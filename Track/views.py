from django.shortcuts import render
from django.http import HttpResponse
from .models import register
# Create your views here.

def all_Track(request):
    return HttpResponse("hey")

def register(request):
    return render(request,'models.py')

def login(request):
     return render(request,'models.py')
