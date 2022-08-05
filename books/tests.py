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


    def test_search_query(self):
        book1 = Book.objects.create(title="kitob1", describtion="descrip1", isbn="121212")
        book2 = Book.objects.create(title="ertak2", describtion="descrip2", isbn="122212")
        book3 = Book.objects.create(title="story3", describtion="descrip3", isbn="123212")

        response = self.client.get(reverse("books:list")+"?q=kitob1")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list")+"?q=ertak2")
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list")+"?q=story3")
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book1.title)

