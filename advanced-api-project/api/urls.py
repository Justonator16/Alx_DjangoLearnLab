from django.urls import path
from api import views

urlpatterns = [
    path("books", views.BookListView.as_view(), name="book_list"),
    path("books/detail/<int:pk>", views.BookDetailView.as_view(), name="book_detail"),
    path("books/create", views.BookCreateView.as_view(), name="book_create"),
    path("books/update/<int:pk>", views.BookUpdateViews.as_view(), name="book_update"),
    path("books/delete/<int:pk>", views.BookDeleteView.as_view(), name="book_delete")
]

