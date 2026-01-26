from django.shortcuts import render
from django.http import HttpResponse
from .models import register

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import EchoSerializer

@api_view(["POST"])
def echo_view(request):
    serializer = EchoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.

def all_Track(request):
    return HttpResponse("hey")

def register(request):
    return render(request,'models.py')

def login(request):
     return render(request,'models.py')
