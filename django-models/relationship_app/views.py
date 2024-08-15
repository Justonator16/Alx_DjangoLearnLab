from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#Function based view
def books(request):
    book_objs = Book.objects.all()

    books = {}
    for book in book_objs:
        books[book.title] = [book.author, book.publication_year]
        
    context = books
    return render(request, 'relationship_app/list_books.html' , context)

class BookView(TemplateView):
    template_name = 'library_detail.html'
