from rest_framework import serializers
from .models import Client, Gender
from django.contrib.auth import get_user_model
User = get_user_model()


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class GetClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['lasID']


    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


