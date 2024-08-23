from django.shortcuts import render
from django.http import HttpReponse
from models import Book

# Create your views here.
def list_books(request):
    book_list = Book.objects.all() 
    if not book_list:
        raise_exception = "Error occured"
        response = HttpReponse(raise_exception)
        response["Content-Security-Policy"] = "default-src 'self';"

    return render(request, 'relationship_app/list_books.html' , context={'books': book_list})
