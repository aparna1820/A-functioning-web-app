# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, UserProfileViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
