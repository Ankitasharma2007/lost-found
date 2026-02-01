from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LostSerializer ,FoundSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LostView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = LostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(rollnumber = request.user.rollnumber)
            return Response({"message":"item registered"}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class FoundView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = FoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(rollnumber = request.user.rollnumber)
            return Response({"message":"item found"}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    