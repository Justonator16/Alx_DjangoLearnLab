from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20 )

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=20,  )
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  )

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library(models.Model):
    name = models.CharField(max_length=20,  )
    books = models.ManyToManyField(Book,  )

    def __str__(self):
        return f"Library name {self.name} {self.books} "
    
class Librarian(models.Model):
    name = models.CharField(max_length=20,  )
    library = models.OneToOneField(Library, on_delete=models.CASCADE,  )

    def __str__(self):
        return f"Librarian name {self.name} , Library {self.library}"

# record = Author(1,"Junior")
# record.save()

# b = Book(id=None, title="1987" , author=record)
# b.save()

# print(b.author.id)
# print(b.author)
