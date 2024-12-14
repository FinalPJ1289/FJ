from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=150, blank=True)
    user_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nickname
