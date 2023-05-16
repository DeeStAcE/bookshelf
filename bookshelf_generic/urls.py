from django.urls import path

from .views import *

urlpatterns = [
    path('book/', BookGenericListView.as_view(), name='book-generic-list'),
    path('author/', AuthorGenericListView.as_view(), name='author-generic-list'),
    path('book/add/', AddBookGenericView.as_view(), name='book-generic-add'),
    path('book/<int:pk>/', BookGenericDetailsView.as_view(), name='book-generic-details'),
    path('publishers/', PublisherGenericListView.as_view(), name='publisher-generic-list'),
    path('publishers/add', PublisherAddGenericView.as_view(), name='publisher-generic-add'),
    path('publishers/<int:pk>', PublisherGenericEditView.as_view(), name='publisher-generic-edit'),
]
