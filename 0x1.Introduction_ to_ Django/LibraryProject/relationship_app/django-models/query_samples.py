from .models import Author, Library, Librarian, Book

# Query all books by a specific author.
author = Author("Joe")
book = Book("1987", author.name)
book.objects.filter()

# List all books in a library.
libary = Library("1987", book.title)

libary.objects.all()

# Retrieve the librarian for a library.
librarian = Librarian("Justo", libary)