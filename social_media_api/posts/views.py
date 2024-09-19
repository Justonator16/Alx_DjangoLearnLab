from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# posts/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics

@api_view(['POST'])
def like_post(request, pk): 
    post = generics.get_object_or_reate(Post, pk=pk)
    user = request.user
    if Like.objects.filter(post=post, user=user).exists():
        return Response({'detail': 'You already liked this post.'}, status=400)

    Like.objects.get_or_create(user=request.user, post=post)
    
    # Create notification for post author
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked your post',
        target=post
    )
    
    return Response({'detail': 'Post liked successfully.'})

@api_view(['POST'])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    user = request.user
    like = Like.objects.filter(post=post, user=user)
    if like.exists():
        like.delete()
        return Response({'detail': 'Post unliked successfully.'})
    return Response({'detail': 'You have not liked this post.'}, status=400)
