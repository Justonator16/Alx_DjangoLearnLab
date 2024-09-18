from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import CustomUserForm
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import generics

class UserListView(ListView, generics.GenericAPIView):
    model = User
    queryset = CustomUser.objects.all()
    template_name = 'accounts/removeme.html'
    context_object_name = 'users'

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


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework import permissions


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.add(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if user_to_unfollow == request.user:
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)



   
    
