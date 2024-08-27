from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("", BookList.as_view(), name="book_list"),
]