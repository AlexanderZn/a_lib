from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('guest/', views.guest),
    path('home/', views.user_home),
    path('admin_home/', views.admin_home)
]

# Authentication/registration urls (login, logout, password management, sign up)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', views.registration),
    path('accounts/sign_up/', views.sign_up),
    path('log_in/', views.log_in)
]