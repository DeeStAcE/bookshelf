from django.urls import path

from .views import *

urlpatterns = [
    path('publishers/', PublishersListView.as_view(), name='publishers-list'),
    path('publishers/add/', PublishersAddView.as_view(), name='publishers-add'),
    path('publishers/edit/<int:id>/', PublishersEditView.as_view(), name='publishers-edit'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/add/', CategoryAddView.as_view(), name='category-add'),
    path('category/edit/<int:id>/', CategoryEditView.as_view(), name='category-edit'),
    path('author/add/', AuthorAddView.as_view(), name='author-add'),
    path('author/', AuthorListView.as_view(), name='author-list'),
    path('author/edit/<int:id>/', AuthorEditView.as_view(), name='author-edit'),
    path('book/add/', AddBookView.as_view(), name='book-add'),
    path('book/', BookListView.as_view(), name='book-list'),
    path('book/<int:id>/', BookDetailsView.as_view(), name='book-details'),
]
