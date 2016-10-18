from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    isbn = models.CharField('ISBN', primary_key=True, max_length=13)
    author = models.ForeignKey(Author, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.name
