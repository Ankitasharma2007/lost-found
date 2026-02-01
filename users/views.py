from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .serializers import LostSerializer
from .serializers import FoundSerializer

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LostView(APIView):
    def post(self, request):
        serializer = LostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"item registered"}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class FoundView(APIView):
    def post(self, request):
        serializer = FoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"item found"}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    