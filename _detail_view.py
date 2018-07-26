# -*- coding: utf-8 -*-

# models.py

from django.db import models


class Article(models.Model):

    name = models.CharField(verbose_name='nome', max_length=30)
    slug = models.SlugField()


# views.py

from django.views.generic.detail import DetailView
from .models import Article


class ArticleDetailView(DetailView):

    # Por padrão o template_name_suffix é '_detail' logo o django buscará por app_name/'article_detail.html'
    model = Article
