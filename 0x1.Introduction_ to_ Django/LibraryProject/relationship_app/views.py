from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Library, Book

# Create your views here.
#Function based view
def list_books(request):
    book_objs = Book.objects.all()
        
    remove_me =  'relationship_app/list_books.html'
    return render(request, 'list_books.html' , context={'books': book_objs})

class BookView(TemplateView):
    x = 'relationship_app/library_detail.html'
    template_name = x

class LibraryDetailView(DetailView):
    x = 'relationship_app/library_detail.html'
    template_name = x

class LibraryListView(ListView):
    x = 'relationship_app/library_detail.html'
    template_name = x

def register(request):
    
    return render(request, "register.html")