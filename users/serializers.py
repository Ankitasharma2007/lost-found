from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Lost,Found

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','password','email','phonenumber','rollnumber']

    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            phonenumber=validated_data.get('phonenumber'),
            rollnumber=validated_data.get('rollnumber'),
        )
        return user
    
class LostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lost
        fields = ['nameofarticle','description','location']

    # def create(self, validated_data):
    #     lost = Lost.objects.create(
    #         rollnumber = validated_data.get('rollnumber'),
    #         nameofarticle = validated_data.get('nameofarticle'),
    #         description = validated_data.get('description'),
    #         location = validated_data.get('location'),
    #     )
    #     return lost

class FoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Found
        fields = ['nameofarticle','description','location']

    # def create(self, validated_data):
    #     found = Found.objects.create(
    #         rollnumber = validated_data.get('rollnumber'),
    #         nameofarticle = validated_data.get('nameofarticle'),
    #         description = validated_data.get('description'),
    #         location = validated_data.get('location'),
    #     )
    #     return found

class LostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = ['id','rollnumber','nameofarticle','description','location','resolved','found_name']

