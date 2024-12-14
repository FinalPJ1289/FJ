from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('mypage/', mypage, name='mypage'),
    path('home/', home, name='home')
]