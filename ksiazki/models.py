from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)


class Author(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=64)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()
