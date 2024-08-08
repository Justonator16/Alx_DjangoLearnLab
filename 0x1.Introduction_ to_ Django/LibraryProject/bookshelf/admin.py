from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ["title","author","publication_year"]
    list_filter = ["author","title","publication_year"]
    search_fields = []

# Register your models here.
admin.site.register(Book, BookAdmin)