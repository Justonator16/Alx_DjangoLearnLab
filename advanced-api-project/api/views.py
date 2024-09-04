from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from .seriealizers import BookSerializer
from django_filters import rest_framework

#Provides a list of all book created from models
class BookListView(IsAuthenticatedOrReadOnly, ListView):
    template_name = 'api/book_list.html'
    model = Book
    context_object_name = "books"

# Returns a detailed book attributes
class BookDetailView(IsAuthenticatedOrReadOnly, DetailView):
    template_name = 'api/book_detail.html'
    model = Book
    context_object_name = "book"

#Create a book but only logged in users are allowed
class BookCreateView(IsAuthenticated , CreateView):
    template_name = 'api/book_create.html'
    model = Book
    form_class = BookForm    
    success_url = reverse_lazy('book_list')

# Only loggedin users are allowed to update a book
class BookUpdateViews(IsAuthenticated , UpdateView):
    template_name = 'api/book_update.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

#Only logged in users are allowed to delete books
class BookDeleteView(IsAuthenticated, DeleteView):
    template_name = 'api/book_delete.html'
    model = Book
    context_object_name = "book"
    success_url = reverse_lazy('book_list')

"""
API SECTION
"""

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [ 
        rest_framework.DjangoFilterBackend, 
        rest_framework.filters.SearchFilter, rest_framework.filters.OrderingFilter]
    filterset_fields = ['title', 'author']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

