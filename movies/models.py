from django.db import models

from djangotoolbox.fields import ListField

# Create your models here.

from djangotoolbox.fields import EmbeddedModelField
class Movie(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    actors = ListField(EmbeddedModelField('Actor') )
    director = EmbeddedModelField('Director') 
    tags = ListField(EmbeddedModelField('Tag'))
    text = models.TextField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    character = models.CharField(max_length=200)

class Director(models.Model):
    name = models.CharField(max_length=200)

class Tag(models.Model):
    name = models.CharField(max_length=200)