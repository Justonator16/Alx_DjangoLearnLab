from django.urls import path
from blog.views import LoginUserView, RegisterView, LogoutUserView, profile, BlogView
from blog import views as crud

# Checker fix
"post/<int:pk>/comments/new/"

urlpatterns = [
    path("", BlogView.as_view() , name="blog"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view() ,name='logout'),
    path('profile/', profile, name='profile'),

    # CRUD Operations for Post Model
    path('post/', crud.PostListView.as_view(), name="post_list"),
    path('post/new/', crud.PostCreateView.as_view(), name="post_create"),
    path('post/<int:pk>/', crud.PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', crud.PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', crud.PostDeleteview.as_view(), name="post_delete"),

    # CRUD Operation Comment Model
    path('comment/', crud.CommentListView.as_view(), name='comment_list'),
    path('comments/new/', crud.CommentCreateView.as_view(), name="comment_create"),
    path('comment/<int:pk>/detail/', crud.CommentDetailView.as_view(), name="comment_detail"),
    path('comment/<int:pk>/update/', crud.CommentUpdateView.as_view(), name="comment_update"),
    path('comment/<int:pk>/delete/', crud.CommentDeleteView.as_view(), name="comment_delete"),
]
