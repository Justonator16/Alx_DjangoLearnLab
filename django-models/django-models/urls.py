"""
URL configuration for django_models project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views
from relationship_app.views import list_books, LibraryDetailView ,LibraryListView ,BookView
from relationship_app.admin_view import admin_view
from relationship_app.librarian_view import librarian_view
from relationship_app.member_view import member_view

urlpatterns = [
    path("", list_books, name="books"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),

    path('admin_view/', admin_view, name='Admin'),
    path('librarian/', librarian_view, name='Librarian'),
    path('member/', member_view, name='Member'),

    path("library/", BookView.as_view(), name="library"),
    path("library_detail/", LibraryDetailView.as_view(), name="library_detail"),
    path("library_list/", LibraryListView.as_view(), name="library_list"),
    path('admin/', admin.site.urls),
]
