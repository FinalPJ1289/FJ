from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 글쓰기 모델
class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="나의 이야기를 들려주세요", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # 추가된 부분

    def __str__(self):
        return self.title
    
# 댓글모델
class Comment(models.Model):
    linked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=300, verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='my_comment')  # 변경된 부분

    def __str__(self):  
        return self.content