from django.shortcuts import render

# Create your views here.
# core/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import App, UserProfile, Task
from .serializers import AppSerializer, UserProfileSerializer, TaskSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

# core/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
