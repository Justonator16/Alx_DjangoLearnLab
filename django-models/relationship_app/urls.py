from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import views
from .views import list_books, LibraryDetailView ,LibraryListView ,BookView
from admin_view import admin_view
from librarian_view import librarian_view
from member_view import member_view

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html")),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),

    path('admin_view/', admin_view, name='Admin'),
    path('librarian/', librarian_view, name='Librarian'),
    path('member/', member_view, name='Member'),

    path('add_book/', views.add_book, name="add_book"),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),

    path("", list_books, name="books"),
    path("library/", BookView.as_view(), name="library"),
    path("library_detail/", LibraryDetailView.as_view(), name="library_detail"),
    path("library_list/", LibraryListView.as_view(), name="library_list"),
]