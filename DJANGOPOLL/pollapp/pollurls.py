from django.contrib import admin
from django.urls import path
from pollapp import views

urlspatterns = [
    path('',views.welcome,name = "welcome")
]