from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Library, Book
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
#Function based view
def list_books(request):
    book_objs = Book.objects.all()
        
    remove_me =  'relationship_app/list_books.html'
    return render(request, 'list_books.html' , context={'books': book_objs})

class BookView(TemplateView):
    template_name = 'relationship_app/library_detail.html'

class LibraryDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/library_detail.html'

class LibraryListView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})


def admin_check(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'admin_view.html')

def member_check(user):
    return user.userprofile.role == 'Member'

@user_passes_test(member_check)
def member_view(request):
    return render(request, 'member_view.html')

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'librarian_view.html')