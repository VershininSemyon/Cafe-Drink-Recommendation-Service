
import uuid
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    about_me = models.TextField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username


class RegistrationToken(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(hours=24)
    
    def __str__(self):
        return f"Токен регистрации {self.token} для {self.email}"
