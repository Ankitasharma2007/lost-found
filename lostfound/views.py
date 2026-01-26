from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return HttpResponse("hello world")
    

def about(request):
    return HttpResponse("this is about page")
    
def contact(request):
    return HttpResponse("you can contact us")

def register(request):
    return render(request,'models.py')

def login(request):
     return render(request,'models.py')