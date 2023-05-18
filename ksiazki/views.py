from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *


# Create your views here.
class MainView(View):

    def get(self, request):
        return render(request, 'main.html')


class PublishersListView(View):

    def get(self, request):
        publishers = Publisher.objects.order_by('name')
        context = {
            'publishers': publishers
        }
        return render(request, 'publishers_list.html', context=context)


class PublishersAddView(View):

    def get(self, request):
        return render(request, 'publishers_add.html')

    def post(self, request):
        name = request.POST.get('name')
        if name:
            Publisher.objects.create(name=name)
        return redirect('publishers-list')


class PublishersEditView(View):

    def get(self, request, id):
        return render(request, 'publishers_add.html',
                      {'publisher': Publisher.objects.get(pk=id)})

    def post(self, request, id):
        name = request.POST.get('name')
        if name:
            publisher = Publisher.objects.get(pk=id)
            publisher.name = name
            publisher.save()
        return redirect('publishers-list')


class CategoryListView(PermissionRequiredMixin, View):
    permission_required = ['ksiazki.view_category']

    def get(self, request):
        categories = Category.objects.order_by('name')
        context = {
            'categories': categories
        }
        return render(request, 'category_list.html', context=context)


class CategoryAddView(View):

    def get(self, request):
        return render(request, 'category_add.html')

    def post(self, request):
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
        return redirect('category-list')


class CategoryEditView(View):

    def get(self, request, id):
        return render(request, 'category_add.html',
                      {'category': Category.objects.get(pk=id)})

    def post(self, request, id):
        name = request.POST.get('name')
        if name:
            category = Category.objects.get(pk=id)
            category.name = name
            category.save()
        return redirect('category-list')


class AuthorListView(View):

    def get(self, request):
        return render(request, 'author_list.html',
                      {'authors': Author.objects.order_by('last_name', 'first_name')})


class AuthorAddView(View):

    def get(self, request):
        form = AddAuthorForm()
        return render(request, 'add_author.html', {'form': form})

    def post(self, request):
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date = form.cleaned_data['date']
            Author.objects.create(first_name=first_name, last_name=last_name, birth_date=date)
            return redirect('author-list')
        return render(request, 'add_author.html', {'form': form})


class AuthorEditView(View):

    def get(self, request, id):
        author = Author.objects.get(pk=id)
        form = AddAuthorForm(initial={'first_name': author.first_name,
                                      'last_name': author.last_name,
                                      'date': author.birth_date})
        return render(request, 'add_author.html', {'form': form})

    def post(self, request, id):
        author = Author.objects.get(pk=id)
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date = form.cleaned_data['date']
            author.first_name, author.last_name, author.birth_date = first_name, last_name, date
            author.save()
            return redirect('author-list')
        return render(request, 'add_author.html', {'form': form})


class AddBookView(View):

    def get(self, request):
        form = AddBookForm()
        return render(request, 'book_add.html', {'form': form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save(commit=False) nie zapisuj obiektu do bazy danych
            return redirect('book-list')
        return render(request, 'book_add.html', {'form': form})


# class BookListView(PermissionRequiredMixin, View):
#     permission_required = ['ksiazki.view_book']
# dodawanie przykładowego dostępu do strony
class BookListView(PermissionRequiredMixin, View):
    permission_required = ['ksiazki.view_book']

    def get(self, request):
        return render(request, 'book_list.html',
                      {'books': Book.objects.order_by('title')})


class BookDetailsView(View):

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = AddCommentForm()
        return render(request, 'book_details.html',
                      {'book': book,
                       'form': form})

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('main')
        book = Book.objects.get(pk=pk)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.user = request.user
            comment.save()
            return redirect('book-details', pk)
        return render(request, 'book_details.html',
                      {'book': book,
                       'form': form})


class EditCommentView(UserPassesTestMixin, View):

    def test_func(self):
        comment = Comment.objects.get(pk=self.kwargs['pk'])
        return comment.user == self.request.user

    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        # if comment.user != request.user:
        #     return redirect('main')
        form = AddCommentForm(instance=comment)
        return render(request, 'form.html', {'form': form})
