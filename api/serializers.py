from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from books.models import Book, BookReview
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'describtion', 'isbn')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class BookReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)    #book serializerning id sini orniga dannilarini olib beradi
    book = BookSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = BookReview
        fields = ("id", "stars_given", "comment", "book", "user", "user_id", "book_id")   
    