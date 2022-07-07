from rest_framework import generics
from books.models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by('last_name')
    serializer_class = AuthorSerializer


class CreateAuthorAPIView(generics.CreateAPIView):
    queryset = Author.objects.all().order_by('last_name')
    serializer_class = AuthorSerializer


class DetailAuthorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all().order_by('last_name')
    serializer_class = AuthorSerializer


class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBookAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer


class DetailBookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
