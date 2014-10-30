#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'TheOcean'

from django.forms import *
from books.models import *

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'email']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'category', 'author']