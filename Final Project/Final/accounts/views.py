from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(request):
    from .forms import SignUpForm
    if request.method == "GET" :
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form':form})

    form = SignUpForm(request.POST)
    # 폼 데이터가 유효하면 자동 로그인 후 홈으로 이동
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('accounts:home')
    else :
        return render(request, 'accounts/signup.html',{'form' : form})
    
def login_view(request) :
    if request.method == "GET" :
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})
    form=AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('accounts:home')
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request) :
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "로그아웃 되었습니다.")
    return redirect('accounts:home')

# 마이페이지는 로그인한 사용자만 접근 가능
@login_required
def mypage(request) :
    return render(request, 'accounts/mypage.html')

def home(request) :
    return render(request, 'accounts/home.html')
