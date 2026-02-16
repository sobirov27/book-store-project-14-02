from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=17, unique=True)
    stock = models.PositiveIntegerField()


    def __str__(self):
        return self.title

