from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Set up test data
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2024,
            author=self.author
        )
        self.url = reverse('book-list')

        # Create and log in a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        data = {'title': 'New Book', 'publication_year': 2024, 'author': self.author.id}
        response = self.client.post(self.url, data, format='json')

        # Check status code and response data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('title', response.data)
        self.assertEqual(response.data['title'], 'New Book')
        self.assertEqual(Book.objects.count(), 2)

    def test_get_books(self):
        response = self.client.get(self.url, format='json')

        # Check status code and response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        data = {'title': 'Updated Book Title'}
        response = self.client.patch(url, data, format='json')

        # Check status code and response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data)
        self.assertEqual(response.data['title'], 'Updated Book Title')

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.delete(url, format='json')

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = f"{self.url}?title=Test Book"
        response = self.client.get(url, format='json')

        # Check status code and response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_search_books(self):
        url = f"{self.url}?search=Test Book"
        response = self.client.get(url, format='json')

        # Check status code and response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_order_books(self):
        url = f"{self.url}?ordering=title"
        response = self.client.get(url, format='json')

        # Check status code and response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')