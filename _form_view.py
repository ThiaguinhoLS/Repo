# -*- coding: utf-8 -*-

# forms.py
from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        pass


# views.py
from django.generic.views.edit import FormView


class ContactView(FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact-success/'

    def form_valid(self, form):
        'Caso o formulário sejá válido'
        form.send_mail()
        return super().form_valid(form)
