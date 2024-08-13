from .models import Author, Library, Librarian, Book

# Query all books by a specific author.
author = Author("Joe")
author_name = author.name
Author.objects.get(name=author_name)

books = Book("1987", author.name)
books.objects.filter(author=author)
books.all()

# List all books in a library.
libary = Library("1987", books.title)
library_name = libary.name
Library.objects.get(name=library_name)

libary.objects.all()

# Retrieve the librarian for a library.
librarian = Librarian("Justo", libary)
Librarian.objects.get(libary=library_name)