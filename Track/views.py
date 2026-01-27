from django.shortcuts import render
from django.http import HttpResponse
from .models import register

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import EchoSerializer,RegisterSerializer

# @api_view(["POST"])
# def register_echo(request):
#     serializer = EchoSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.

def all_Track(request):
    return HttpResponse("hey")

def RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"user regitered"},status=201)
        return Response(serializer.errors,status=400)

def login(request):
     return render(request,'models.py')
