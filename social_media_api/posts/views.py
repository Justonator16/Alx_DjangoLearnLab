from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

# CRUD OPERATIONS API
# Create API
class PostCreateAPIView(CreateAPIView):
    serializer_class = CreateAPIView

# View all posts 
class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer

# Update a post
class PostUpdateView(UpdateAPIView):
    serializer_class = PostSerializer

# Delete a post
class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostSerializer

# Comment crud

class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer

# View all posts 
class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer

# Update a post
class CommentUpdateView(UpdateAPIView):
    serializer_class = CommentSerializer

# Delete a post
class CommentDestroyAPIView(DestroyAPIView):
    serializer_class = CommentSerializer


    


