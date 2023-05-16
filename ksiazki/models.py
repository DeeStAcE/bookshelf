from django.db import models
from django.urls import reverse


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=64)

    # pozyskaj adres url dla szczegółów danego obiektu (get_detail_url)
    def get_absolute_url(self):
        return reverse('publisher-generic-edit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('category-edit', kwargs={'id': self.id})

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()

    def get_absolute_url(self):
        return reverse('author-edit', kwargs={'id': self.id})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=64)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()

    def get_absolute_url(self):
        return reverse('book-generic-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
