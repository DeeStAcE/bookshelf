from django.test import Client
from django.urls import reverse

from ksiazki.conftest import *

from ksiazki.models import Book


# Create your tests here.
@pytest.mark.django_db
def test_book_edit_get_method(book_fixture):
    client = Client()
    url = reverse('book-generic-details', kwargs={'pk': book_fixture.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_edit_post_method(book_fixture, publishers_fixture, categories_fixture, author_fixture):
    client = Client()
    url = reverse('book-generic-details', kwargs={'pk': book_fixture.id})
    data = {
        'title': 'new_test_title',
        'year': 2020,
        'author': author_fixture[1].id,
        'publisher': publishers_fixture[1].id,
        'categories': [cat.id for cat in categories_fixture]
    }
    response = client.post(url, data)
    redirect_url = reverse('book-generic-list')
    assert response.status_code == 302
    assert response.url.startswith(redirect_url)
    try:
        Book.objects.get(title=book_fixture.title)
        assert False
    except Book.DoesNotExist:
        assert True
    updated_book = Book.objects.get(title='new_test_title')
    assert book_fixture.id == updated_book.id
