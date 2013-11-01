from django.db import models

from djangotoolbox.fields import ListField

# Create your models here.

from djangotoolbox.fields import EmbeddedModelField
class Movie(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    actors = ListField(EmbeddedModelField('Actor') )
    director = EmbeddedModelField('Director') 
    tags = ListField(EmbeddedModelField('Tag'))
    text = models.TextField()
    title = models.CharField()
    year = models.CharField()


class Actor(models.Model):
    name = models.CharField()
    character = models.CharField()

class Director(models.Model):
    name = models.CharField()

class Tag(models.Model):
    name = models.CharField()