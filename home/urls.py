from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',  views.home_page, name='home'),
    path('test/', views.test, name='test'),
    path('profile', views.profile, name='profile')
]
