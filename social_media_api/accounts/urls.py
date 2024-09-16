from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('log/', views.LoginView.as_view() , name="login"),
    path('register/', views.RegisterUserView.as_view()  , name="register"),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view()  , name="profile_detail"),
    path('profile/create', views.ProfileView.as_view(), name='profile_create'),

    #Serializer
    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('api/login/', views.CustomAuthToken.as_view(), name='api_login'),
]
