#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from books.models import *
from books.forms import *
from books.serializers import *
from rest_framework import viewsets

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def list_books(request):
    books = Book.objects.all().order_by('title')

    return render(request, 'book_list.html', {'p_title':'The Book Archive', 'books':books})

def add_author(request):
    author = Author()

    if request.method == 'POST':
        #provjeri formu
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()  #iščitaj formu kasnije
            messages.success(request, u'Epic success! Author added.')
            return HttpResponseRedirect(reverse('bookList'))  # vraća na prethodni view
        else:
            messages.error(request, u'Nešto nije uneseno kak spada!')#forma nije validna
            pass
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author.html', {'p_title':'Add Author', 'form': form})

def edit_book(request, pk=None):
    if pk==None:
        book = Book()
    else:
        book = get_object_or_404(Book, pk=pk)

    if request.method=='POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, u'Epic success! Book edited.')
            return HttpResponseRedirect(reverse('bookList'))
        else:#forma nije validna
            messages.error(request, u'Nešto s knjigom nije uneseno kak spada!')
            pass
    else:
        form = BookForm(instance=book)
        return render(request, 'book.html', {'p_title':'Book details', 'form':form})