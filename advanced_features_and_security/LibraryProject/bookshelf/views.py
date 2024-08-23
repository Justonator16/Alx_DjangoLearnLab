from django.shortcuts import render
from models import Book

# Create your views here.
def list_books(request):
    book_list = Book.objects.all() 
    if not book_list:
        raise

    return render(request, 'relationship_app/list_books.html' , context={'books': book_list})
