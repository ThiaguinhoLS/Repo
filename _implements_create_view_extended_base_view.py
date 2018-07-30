# -*- coding: utf-8 -*-

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/article/', views.ArticleCreateView.as_view(), name='create_article'),
]


# models.py

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Article(models.Model):

    name = models.CharField(verbose_name='nome', max_length=30)
    slug = models.SlugField()  # Por padrão o campo slug define max_length = 50
    user = models.ForeignKey(
        verbose_name='usuário',
        to=User,
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse('detail', args=(self.pk,))

    def __str__(self):
        return self.name


# forms.py

from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('user',)


# views.py

from django.views.generic.base import View
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import ArticleModelForm
from django.core.exceptions import ImproperlyConfigured


class _CreateView(View):

	object = None
    form_class = None
    template_name = None
    success_url = None

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        if self.success_url:
            url = self.success_url
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    'Defina o atributo de classe success_url ou '
                    'o método get_absolute_url no seu modelo'
            )
        return url
