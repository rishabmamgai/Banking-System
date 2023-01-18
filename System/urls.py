from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.login, name='Log In'),
    path('create_account/', views.create_account, name='Create Account'),
    path('transaction/', views.transaction, name='Transaction')
]
