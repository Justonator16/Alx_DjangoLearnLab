from typing import Any
from django.db import models

# Create your models here.

class Author(models.Model):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = models.CharField(max_length=20)

class Book(models.Model):
    def __init__(self, title: str, author: str):
        super().__init__()

        self.title = models.CharField(max_length=20)
        self.author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author
    
class Library(models.Model):
    def __init__(self, name: str, books: str) -> None:
        super().__init__()

        self.name = models.CharField(max_length=20)
        self.books = models.ManyToManyField(Book)

    def __str__(self):
        return self.books
    
class Librarian(models.Model):
    def __init__(self, name: str, library: str):
        super().__init__()
        
        self.name = models.CharField(max_length=20)
        self.library = models.OneToOneField(Library)

    def __str__(self):
        return self.library