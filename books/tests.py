from django.test import TestCase
from django.urls import reverse

from books.models import Book


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))

        self.assertContains(response, "No books found.")


    def test_books_list(self):
        Book.objects.create(title="book1", describtion="descrip1", isbn="121212")
        Book.objects.create(title="book2", describtion="descrip2", isbn="122212")
        Book.objects.create(title="book3", describtion="descrip3", isbn="123212")
     
        response = self.client.get(reverse("books:list"))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    
    def test_detail_page(self):
        book = Book.objects.create(title="book1", describtion="descrip3", isbn="123212")

        response = self.client.get(reverse("books:detail", kwargs={"id": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.describtion)
