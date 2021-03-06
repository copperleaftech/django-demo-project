from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    isbn = models.CharField('ISBN', primary_key=True, max_length=13)
    author = models.ForeignKey(Author, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', kwargs=dict(pk=self.pk))
