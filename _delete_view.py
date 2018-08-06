# -*- coding: utf-8 -*-

# models.py

from django.db import models


class Author(models.Model):

    name = models.CharField(verbose_name='nome', max_length=30)
    age = models.PositiveSmallIntegerField(verbose_name='idade', blank=True)


# views.py

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Author


class AuthorDelete(DeleteView):

    # Por padrão é '_confirm_delete', agora será 'author_check_delete.html'
    template_name_suffix = '_check_delete'
    model = Author
    success_url = reverse_lazy('index')
