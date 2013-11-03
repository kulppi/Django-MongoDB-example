from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.

from djangotoolbox.fields import EmbeddedModelField
class Movies(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    tags = ListField(EmbeddedModelField('Tag'))
    text = models.TextField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    synopsis = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    character = models.CharField(max_length=200)

class Director(models.Model):
    name = models.CharField(max_length=200)

class Tag(models.Model):
    name = models.CharField(max_length=200)