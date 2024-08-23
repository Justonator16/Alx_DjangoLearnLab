from django.shortcuts import render
from django.http import HttpReponse
from models import Book

# Create your views here.
def list_books(request):
    book_list = Book.objects.all() 
    if not book_list:
        raise_exception = "Error occured"
        return HttpReponse(raise_exception)

    return render(request, 'relationship_app/list_books.html' , context={'books': book_list})
