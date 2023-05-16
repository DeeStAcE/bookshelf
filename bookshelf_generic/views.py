from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from ksiazki.forms import AddBookForm
from ksiazki.models import *


# Create your views here.

class BookGenericListView(ListView):
    model = Book
    template_name = 'list_view.html'

    def get_queryset(self):
        return super().get_queryset().order_by('title')


class BookGenericDetailsView(UpdateView):
    model = Book
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-generic-list')


class AddBookGenericView(CreateView):
    model = Book
    form_class = AddBookForm  # w celu stworzenia customowego formularza
    template_name = 'form.html'
    success_url = reverse_lazy('book-generic-list')


class AuthorGenericListView(ListView):
    model = Author
    template_name = 'list_view.html'


class PublisherGenericListView(ListView):
    model = Publisher
    template_name = 'list_view.html'

    def get_queryset(self):
        return super().get_queryset().order_by('name')


class PublisherAddGenericView(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('publisher-generic-list')


class PublisherGenericEditView(UpdateView):
    model = Publisher
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('publisher-generic-list')
