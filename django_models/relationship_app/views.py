from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
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
    model = Book
    template_name = x

class LibraryListView(ListView):
    x = 'relationship_app/library_detail.html'
    template_name = x

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})