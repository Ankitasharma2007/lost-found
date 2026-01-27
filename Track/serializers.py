from rest_framework import serializers
from .models import register
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = register
        fields = ["name", "rollnumber", "email", "phonenumber", "user_id", "set_password"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        registered = register.objects.create(**validated_data)
        return registered
