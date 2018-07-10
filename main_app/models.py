from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


# Create your models here.
class Genre(models.Model):

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Book(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    rating = models.FloatField(blank=True, default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Comments(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)


class UserBook(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    obtaining_date = models.DateTimeField(default=datetime.now, blank=True)
    # status = True (1) if obtained, else status = False (0) 
    status = models.BooleanField(default=1)
