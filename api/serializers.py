from rest_framework import serializers
from books.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('last_name', 'first_name')
