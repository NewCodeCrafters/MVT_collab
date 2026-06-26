from django.urls import path
from . import views

urlpattern = [
    path('user/sign_up', views.sign_up, name='sign_up'),
    path('user/login', views.login, name='login'),
]