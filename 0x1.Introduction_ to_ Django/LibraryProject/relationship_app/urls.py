from django.urls import path
from relationship_app import views
from .views import books, BookView

urlpatterns = [
    path("", views.books, name="books"),
    path("library/", BookView.as_view(), name="library"),
]