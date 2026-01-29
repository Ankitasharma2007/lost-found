from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','password','email','phonenumber','rollnumber']

    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phonenumber=validated_data.get('phonenumber'),
            rollnumber=validated_data.get('rollnumber'),
        )
        return user
    
    