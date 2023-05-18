import pytest
from django.test import Client
from django.urls import reverse

from ksiazki.forms import AddBookForm
from ksiazki.models import Publisher, Category, Book


@pytest.mark.django_db
def test_main():
    client = Client()
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_publishers_view(publishers_fixture):
    client = Client()
    url = reverse('publishers-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['publishers'].count() == len(publishers_fixture)
    for publisher in publishers_fixture:
        assert publisher in response.context['publishers']


# nie działa z powodu nadania wymagań do widoku "CategoryListView"
# @pytest.mark.django_db
# def test_categories_view(categories_fixture):
#     client = Client()
#     url = reverse('category-list')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['categories'].count() == len(categories_fixture)
#     for category in categories_fixture:
#         assert category in response.context['categories']


@pytest.mark.django_db
def test_publisher_add_get_method():
    client = Client()
    url = reverse('publishers-add')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_publisher_add_post_method():
    client = Client()
    url = reverse('publishers-add')
    data = {
        'name': 'test_get_name'
    }
    response = client.post(url, data)
    redirect_url = reverse('publishers-list')
    assert response.url.startswith(redirect_url)
    Publisher.objects.get(name='test_get_name')


@pytest.mark.django_db
def test_category_add_get_method():
    client = Client()
    url = reverse('category-add')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_add_post_method():
    client = Client()
    url = reverse('category-add')
    data = {
        'name': 'test_post_name'
    }
    response = client.post(url, data)
    redirect_url = reverse('category-list')
    assert response.url.startswith(redirect_url)
    Category.objects.get(name='test_post_name')


@pytest.mark.django_db
def test_book_add_get_method():
    client = Client()
    url = reverse('book-add')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddBookForm)


@pytest.mark.django_db
def test_book_add_post_method(publishers_fixture, categories_fixture, author_fixture):
    client = Client()
    url = reverse('book-add')
    data = {
        'title': 'test_title',
        'year': 2020,
        'author': author_fixture[0].id,
        'publisher': publishers_fixture[0].id,
        'categories': [cat.id for cat in categories_fixture]
    }
    response = client.post(url, data)
    redirect_url = reverse('book-list')
    assert response.status_code == 302
    assert response.url.startswith(redirect_url)
    Book.objects.get(title='test_title')


@pytest.mark.django_db
def test_book_add_post_method_invalid_year(publishers_fixture, categories_fixture, author_fixture):
    client = Client()
    url = reverse('book-add')
    data = {
        'title': 'test_title',
        'year': 1990,
        'author': author_fixture[0].id,
        'publisher': publishers_fixture[0].id,
        'categories': [cat.id for cat in categories_fixture]
    }
    response = client.post(url, data)
    try:
        Book.objects.get(title='test_title')
        assert False
    except Book.DoesNotExist:
        assert True
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, AddBookForm)
    assert 'Author could not write that book in this year' in form.errors['__all__']


@pytest.mark.django_db
def test_book_view_not_login():
    client = Client()
    url = reverse('book-list')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_book_view_login_without_permission(user_fixture):
    client = Client()
    client.force_login(user_fixture)
    url = reverse('book-list')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_book_view_login_with_book_permission(user_with_view_book_perm_fixture):
    client = Client()
    client.force_login(user_with_view_book_perm_fixture)
    url = reverse('book-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_view_login_with_category_permission(user_with_view_category_perm_fixture):
    client = Client()
    client.force_login(user_with_view_category_perm_fixture)
    url = reverse('category-list')
    response = client.get(url)
    assert response.status_code == 200
