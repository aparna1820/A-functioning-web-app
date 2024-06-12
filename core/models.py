from django.db import models

# Create your models here.
# core/models.py

from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    name = models.CharField(max_length=100)
    package_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    points_earned = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"
