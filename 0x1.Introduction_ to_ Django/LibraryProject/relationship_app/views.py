from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Library, Book

# Create your views here.
#Function based view
def list_books(request):
    book_objs = Book.objects.all()

    books = {}
    for book in book_objs:
        books[book.title] = [book.author, book.publication_year]
        
    context = books
    remove_me =  'relationship_app/list_books.html'
    return render(request, 'list_books.html' , context)

class BookView(TemplateView):
    x = 'relationship_app/library_detail.html'
    template_name = 'library_detail.html'


class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'

class LibraryListView(ListView):
    template_name = 'relationship_app/library_detail.html'
