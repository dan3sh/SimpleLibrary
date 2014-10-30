#!/usr/bin/env python
# -*- encoding: utf-8 -*-

__author__ = 'TheOcean'

from books.models import Author
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'email']