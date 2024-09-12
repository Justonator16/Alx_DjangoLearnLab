from django.urls import path
from blog.views import LoginUserView, RegisterView, LogoutUserView, profile, BlogView
from blog import views as crud

urlpatterns = [
    path("", BlogView.as_view() , name="blog"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/login', LogoutUserView.as_view() ,name='logout'),
    path('profile/', profile, name='profile'),

    # CRUD Operations for Post Model
    path('login/posts/', crud.PostListView.as_view(), name="post_list"),
    path('login/posts/new', crud.PostCreateView.as_view(), name="post_create"),
    path('login/posts/<int:pk>/', crud.PostDetailView.as_view(), name="post_detail"),
    path('login/posts/<int:pk>', crud.PostUpdateView.as_view(), name="post_update"),
    path('login/posts/<int:pk>/delete', crud.PostDeleteview.as_view(), name="post_delete"),
]
