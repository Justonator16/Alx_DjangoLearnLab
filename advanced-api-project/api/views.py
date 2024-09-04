from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from .forms import BookForm
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .seriealizers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

#Provides a list of all book created from models
class BookListView(IsAuthenticatedOrReadOnly, generic.ListView):
    template_name = 'api/book_list.html'
    model = Book
    context_object_name = "books"

# Returns a detailed book attributes
class BookDetailView(IsAuthenticatedOrReadOnly, generic.DetailView):
    template_name = 'api/book_detail.html'
    model = Book
    context_object_name = "book"

#Create a book but only logged in users are allowed
class BookCreateView(IsAuthenticated , generic.CreateView):
    template_name = 'api/book_create.html'
    model = Book
    form_class = BookForm    
    success_url = reverse_lazy('book_list')

# Only loggedin users are allowed to update a book
class BookUpdateViews(IsAuthenticated , generic.UpdateView):
    template_name = 'api/book_update.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

#Only logged in users are allowed to delete books
class BookDeleteView(IsAuthenticated, generic.DeleteView):
    template_name = 'api/book_delete.html'
    model = Book
    context_object_name = "book"
    success_url = reverse_lazy('book_list')

"""
API SECTION
"""

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

