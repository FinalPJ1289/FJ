from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #이메일
    email = models.EmailField(
        max_length=30,
        unique=True,
        null = False,
        blank = False,
    )
    #닉네임
    nickname = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f'{self.username}'