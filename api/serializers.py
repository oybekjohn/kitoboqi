from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField()
    describtion = serializers.CharField()
    isbn = serializers.CharField()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()


class BookReviewSerializer(serializers.Serializer):
    stars_given = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField()
    book = BookSerializer()
    user = UserSerializer()
    