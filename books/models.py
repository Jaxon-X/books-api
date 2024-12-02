from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    price = models.IntegerField(default=0)

    def __str__(self):
        return  self.title



