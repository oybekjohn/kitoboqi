from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from books.models import Book, BookReview
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "describtion", "isbn", "cover_picture"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "profile_picture"]


class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer() #book serializerning id sini orniga dannilarini olib beradi
    user = UserSerializer()
    class Meta:
        model = BookReview
        fields = ("stars_given", "comment", "book", "user", "created_at")   
    