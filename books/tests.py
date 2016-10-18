from django.test import TestCase
from .factories import *
from .models import *

class DemoTestCase(TestCase):
    def setUp(self):
        self.author_with_no_books = AuthorFactory.create()
        self.author_with_one_book = AuthorFactory.create()
        self.author_with_three_books = AuthorFactory.create()

        BookFactory.create(author=self.author_with_one_book)

        BookFactory.create(author=self.author_with_three_books)
        BookFactory.create(author=self.author_with_three_books)
        BookFactory.create(author=self.author_with_three_books)

    def test_setup(self):
        book_count = Book.objects.filter(author=self.author_with_no_books).count()
        self.assertEqual(book_count, 0)

        book_count = Book.objects.filter(author=self.author_with_one_book).count()
        self.assertEqual(book_count, 1)

        book_count = Book.objects.filter(author=self.author_with_three_books).count()
        self.assertEqual(book_count, 3)
