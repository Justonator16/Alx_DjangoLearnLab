from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import CustomUserForm
from .models import CustomUser

# SERIALIZERS
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer


# SERIALIZER VIEWS

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = get_user_model().objects.get(username=request.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key})


# NORMAL VIEWS
#register a user
class RegisterUserView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = CustomUserForm
    context_object_name = 'form'
    success_url = reverse_lazy('login')

class LoginUserView(LoginView):
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

   
    
