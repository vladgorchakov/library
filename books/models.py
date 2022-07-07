from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.author} - {self.title}'
