from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import CustomUserForm
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView

class RegisterCreateAPIView(CreateAPIView):
    ...

# NORMAL VIEWS
#register a user
class RegisterUserView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = CustomUserForm
    context_object_name = 'form'
    success_url = reverse_lazy('login')

class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('posts')
    
class ProfileView(ListView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'fields'

class CreateProfileView(CreateView):
    template_name = 'accounts/create_profile.html'
    model = User
    form_class = CustomUserForm
    context_object_name = 'form'
    success_url = reverse_lazy('posts')

class ProfileDetailView(DetailView):
    template_name = 'accounts/profile.html'
    model = CustomUser
    context_object_name = 'user_profile'

   
    
