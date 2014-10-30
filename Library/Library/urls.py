# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from books.views import AuthorViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'^books/$', 'books.views.list_books', name='bookList'),
    url(r'^Author/Add/$', 'books.views.add_author', name='addAuthor'),
    url(r'^Book/Add/$', 'books.views.edit_book', name='addBook'),
    url(r'^Book/Edit/(?P<pk>[0-9]+)/?$', 'books.views.edit_book', name='editBook'),
    url(r'^', include(router.urls)),
)
