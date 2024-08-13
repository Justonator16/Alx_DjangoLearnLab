from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library)

# Query all books by a specific author.
author = Author("Joe")
book = Book("1987", author.name)
book.objects.filter()

# List all books in a library.
libary = Library("1987", book.title)

libary.objects.all()

# Retrieve the librarian for a library.
librarian = Librarian("Justo", libary)

