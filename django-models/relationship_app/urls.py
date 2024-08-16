from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import views
from .views import list_books, LibraryDetailView ,LibraryListView ,BookView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html")),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),

    path("", list_books, name="books"),
    path("library/", BookView.as_view(), name="library"),
    path("library_detail/", LibraryDetailView.as_view(), name="library_detail"),
    path("library_list/", LibraryListView.as_view(), name="library_list"),
]