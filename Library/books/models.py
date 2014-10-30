#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u"{} {}".format(self.name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=127)
    category = models.ForeignKey(Category)
    author = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title
