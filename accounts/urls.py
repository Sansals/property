from django.urls import path
from django.shortcuts import render
from .views import *

urlpatterns = [
    path('signup/', create_user, name='signup'),
    path('auth/', auth_user, name='auth')
]