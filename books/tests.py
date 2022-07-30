from django.test import TestCase
from django.urls import reverse

from books.models import Book


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))

        self.assertContains(response, "No books found.")


    def test_books_list(self):
        book1 = Book.objects.create(title="book1", describtion="descrip1", isbn="121212")
        book2 = Book.objects.create(title="book2", describtion="descrip2", isbn="122212")
        book3 = Book.objects.create(title="book3", describtion="descrip3", isbn="123212")
     
        response = self.client.get(reverse("books:list"))

        
        for book in [book1, book2]:
            self.assertContains(response, book.title)

        response = self.client.get(reverse("books:list") + "?page=1")

        self.assertContains(response, book3.title)

    
    def test_detail_page(self):
        book = Book.objects.create(title="book1", describtion="descrip3", isbn="123212")

        response = self.client.get(reverse("books:detail", kwargs={"id": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.describtion)
