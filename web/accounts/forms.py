from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # 커스텀 User 모델 가져오기

# 회원가입 폼
class SignUpForm(UserCreationForm):
    user_id = forms.CharField(
        label="아이디",
        max_length=10,
        widget=forms.TextInput(attrs={"placeholder": "아이디를 입력하세요"}),
    )
    nickname = forms.CharField(
        label="사용자 이름",
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "사용자 이름을 입력하세요"}),
    )

    class Meta:
        model = User
        fields = ["user_id", "nickname"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['user_id']  # user_id를 username으로 설정
        if commit:
            user.save()
        return user

