from django.urls import path
from blog.views import LoginUserView, RegisterView, LogoutUserView, profile, BlogView
from blog import views as crud

urlpatterns = [
    path("", BlogView.as_view() , name="blog"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/login/', LoginUserView.as_view(), name='login'),
    path('logout/login', LogoutUserView.as_view() ,name='logout'),
    path('profile/', profile, name='profile'),

    # CRUD Operations for Post Model
    path('login/post/', crud.PostListView.as_view(), name="post_list"),
    path('login/post/new/', crud.PostCreateView.as_view(), name="post_create"),
    path('login/post/<int:pk>/', crud.PostDetailView.as_view(), name="post_detail"),
    path('login/post/<int:pk>/update/', crud.PostUpdateView.as_view(), name="post_update"),
    path('login/post/<int:pk>/delete/', crud.PostDeleteview.as_view(), name="post_delete"),

    # CRUD Operation Comment Model
    path('login/post/<int:pk>/comment/', crud.CommentListView.as_view(), name='comment_list'),
    path('login/post/<int:pk>/comment/new/', crud.CommentCreateView.as_view(), name="comment_create"),
    path('login/post/<int:pk>/comment/<int:pk>/detail/', crud.CommentDetailView.as_view(), name="comment_detail"),
    path('login/post/<int:pk>/comment/<int:pk>/update/', crud.CommentUpdateView.as_view(), name="comment_update"),
    path('login/post/<int:pk>/comment/<int:pk>/delete/', crud.CommentDeleteView.as_view(), name="comment_delete"),
]
