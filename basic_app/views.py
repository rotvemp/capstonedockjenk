from django.shortcuts import render
from django.views.generic import (
                                View, TemplateView,
                                 ListView, DetailView,
                                 CreateView, UpdateView,
                                 DeleteView)
from django.urls import reverse_lazy
from . import models



class AuthorList(ListView):
    content_object_name = 'author'
    model = models.Author


class AuthorDelete(DeleteView):
    model = models.Author
    success_url = reverse_lazy('basic_app:list')