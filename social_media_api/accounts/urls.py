from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.LoginView.as_view() , name="login"),
    path('register/', views.RegisterUserView.as_view()  , name="register"),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view()  , name="profile_detail"),
    path('profile/create', views.ProfileView.as_view(), name='profile_create'),

    #Serializer
    path('api/register/', views.RegisterCreateAPIView.as_view(), name='api_register'),

    #Follow and unfollow users
    path('all_user/', views.UserListView.as_view(), name='all_users'),
    path('follow/<int:user_id>/', views.follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow-user'),
]
