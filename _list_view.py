# -*- coding: utf-8 -*-

# models.py

from django.db import models


class Article(models.Model):

    name = models.CharField(verbose_name='nome', max_length=30)
    slug = models.SlugField()


# views.py

from django.views.generic.list import ListView
from django.utils import timezone
from .models import Article


class ArticleListView(ListView):

    model = Article
    paginate_by = 100
    # Por padrão template_name_suffix é '_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
