from django.urls import path
from django.views.generic import RedirectView
from .views import *

app_name = 'community'

urlpatterns = [
    path('', RedirectView.as_view(url='/community/0/1/', permanent=True)),
    path('<int:category_id>/<int:sort_by>/', community, name='community'),
    path('create_post/', create_post, name='create_post'),
    path('edit_post/<int:id>/', edit_post, name='edit_post'),

]