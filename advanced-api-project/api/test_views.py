from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

# Create your tests here.
class BookAPITests(TestCase):

    def setup(self):
        self.client = APIClient()
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2004)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2013)

    def test_create_book(self):
        data = {'title': "Book Three", "author": "Author Three", "publication_year": 2020}
        response = self.client.post(reverse('book_list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_get_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        data = {"title": "Updated Book One"}
        response = self.client.patch(reverse('book-detail', kwargs={'pk': self.book1.id}), data)
        self.book1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        response = self.client.get(reverse('book-list'), {'author': 'Author One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author One')

    def test_search_books(self):
        response = self.client.get(reverse('book-list'), {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books(self):
        response = self.client.get(reverse('book-list'), {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2010)



