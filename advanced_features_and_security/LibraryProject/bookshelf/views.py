from django.shortcuts import render
from django.http import HttpReponse
from models import Book
from .forms import ExampleForm

# Create your views here.
def list_books(request):
    book_list = Book.objects.all() 
    if not book_list:
        raise_exception = "Error occured"
        response = HttpReponse(raise_exception)
        response["Content-Security-Policy"] = "default-src 'self';"

    return render(request, 'relationship_app/list_books.html' , context={'books': book_list})

def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)

        if form.is_valid() == True:
            form.save()
            return render(request, "bookshelf/book_list.html")
        else:
            return HttpReponse("An error occured Invalid Input.")
    else:
        form = ExampleForm()
        return render(request, "bookshelf/form_example.html", {"form": form})
