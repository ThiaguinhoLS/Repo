# -*- coding: utf-8 -*-

# models.py
from django.db import models


class Author(models.Model):

    name = models.CharField(verbose_name='nome', max_length=30)
    age = models.PositiveSmallIntegerField(verbose_name='idade', blank=True)


# views.py

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Author


class AuthorCreate(CreateView):

    # Nesse caso o template_name será 'author_create_form.html'
    template_name_suffix = '_create_form'
    model = Author
    fields = ('name',)
    success_url = reverse_lazy('index')
