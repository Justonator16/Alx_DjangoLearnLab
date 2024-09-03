from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin

#Provides a list of all book created from models
class BookListView(generic.ListView):
    template_name = 'api/book_list.html'
    model = Book
    context_object_name = "books"

# Returns a detailed book attributes
class BookDetailView(generic.DetailView):
    template_name = 'api/book_detail.html'
    model = Book
    context_object_name = "book"

#Create a book but only logged in users are allowed
class BookCreateView(LoginRequiredMixin , generic.CreateView):
    template_name = 'api/book_create.html'
    model = Book
    form_class = BookForm    
    success_url = reverse_lazy('book_list')

# Only loggedin users are allowed to update a book
class BookUpdateViews(LoginRequiredMixin , generic.UpdateView):
    template_name = 'api/book_update.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')

#Only logged in users are allowed to delete books
class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'api/book_delete.html'
    model = Book
    context_object_name = "book"
    success_url = reverse_lazy('book_list')


