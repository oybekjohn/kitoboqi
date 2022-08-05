from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=255)
    describtion = models.TextField(verbose_name="Kitobga ta'rif")
    isbn = models.CharField(max_length=17)
    cover_picture = models.ImageField(default="default_book_pic.png")

    class Meta:
        ordering = ["title", "isbn"]

    def get_title(self):
        return self.title

    def __str__(self) -> str:
        return f'{self.title}'


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()

    def get_detail(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.book.title} - {self.author.get_detail()}'



class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_book_title(self):
        return self.book.title

    def __str__(self) -> str:
        return f'{self.book.title} stared by {self.user.username}'
