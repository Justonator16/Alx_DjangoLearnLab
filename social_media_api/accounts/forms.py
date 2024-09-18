from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

