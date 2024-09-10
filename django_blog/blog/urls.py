from django.urls import path
from blog.views import LoginUserView, RegisterView, LogoutUserView, profile, BlogView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view() ,name='logout'),
    path('profile/', profile, name='profile'),
    path('login/blog/', BlogView.as_view(), name='blog'),
]
