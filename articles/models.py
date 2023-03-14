from django.db import models
from django import forms

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        words = self.body.split()
        if len(words) > 50:
            snippet = ' '.join(words[:50]) + '...'
        else:
            snippet = ' '.join(words)
        return snippet

class Archive(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

