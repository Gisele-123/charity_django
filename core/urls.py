# core/urls.py
from django.urls import path
from .views import UserRegistrationView
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
]
