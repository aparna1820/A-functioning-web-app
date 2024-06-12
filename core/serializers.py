# core/serializers.py

from rest_framework import serializers
from .models import App, UserProfile, Task
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture', 'points_earned']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        return data_dict
