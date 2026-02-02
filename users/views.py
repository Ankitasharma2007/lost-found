from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LostSerializer ,FoundSerializer,LostListSerializer,FoundListSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Lost , Found

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

class LostListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        query = Lost.objects.filter(resolved = False)
        serializer = LostListSerializer(query,many=True)
        return Response(serializer.data)
    
class FoundListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        query = Found.objects.filter(lost_item__isnull = True)
        serializer = FoundListSerializer(query,many=True)
        return Response(serializer.data)
    
class MatchLostFoundView(APIView):
    permission_classes = [IsAdminUser]

    def post(self,request):
        lost_id = request.data.get("lost_id")
        found_id = request.data.get("found_id")

        if not lost_id or not found_id : 
            return Response(
                {
                    "error": "Pls send a valid requst"
                },
                status= status.HTTP_400_BAD_REQUEST
            )

        lost_obj = get_object_or_404(Lost,lost_id)
        found_obj = get_object_or_404(Found,found_id)

        lost_obj.resolved = True
        lost_obj.found_item = found_obj
        lost_obj.save()

        return Response(
            {
                "object matched successful"
            },status=status.HTTP_200_OK
        )

        

