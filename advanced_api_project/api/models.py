from django.db import models

# Create your models here.
# Create an Author Table
class Author(models.Model):
    name = models.CharField(max_length=100)

# Create a Book table in database
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, max_length=100)
