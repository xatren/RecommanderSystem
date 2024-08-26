# recommendations/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = ('user', 'item')
