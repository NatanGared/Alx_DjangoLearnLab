from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2023-01-01',
            'isbn': '1234567890123'
        }

    def test_create_book(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('book-create'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_retrieve_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.get(reverse('book-detail', args=[book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = {'title': 'Updated Book'}
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(reverse('book-update', args=[book.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated Book')

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('book-delete', args=[book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        Book.objects.create(title='Another Book', author='Test Author', published_date='2023-01-01', isbn='1234567890124')
        response = self.client.get(reverse('book-list'), {'title': 'Another Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        Book.objects.create(title='Harry Potter', author='J.K. Rowling', published_date='2001-07-21', isbn='1234567890125')
        response = self.client.get(reverse('book-list'), {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        Book.objects.create(title='B Book', author='Author A', published_date='2022-01-01', isbn='1234567890126')
        Book.objects.create(title='A Book', author='Author B', published_date='2022-01-02', isbn='1234567890127')
        response = self.client.get(reverse('book-list'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'A Book')

    def test_permissions(self):
        response = self.client.post(reverse('book-create'), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should be forbidden without login