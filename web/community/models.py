from django.db import models
from django.contrib.auth.models import User

# 글쓰기 모델
class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="나의 이야기를 들려주세요", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title

# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name