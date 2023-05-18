from datetime import datetime

import pytest
from django.contrib.auth.models import User, Permission

from ksiazki.models import Publisher, Category, Author, Book


@pytest.fixture
def publishers_fixture():
    lst = []
    lst.append(Publisher.objects.create(name='ala'))
    lst.append(Publisher.objects.create(name='gosia'))
    lst.append(Publisher.objects.create(name='kasia'))
    return lst


@pytest.fixture()
def categories_fixture():
    lst = []
    lst.append(Category.objects.create(name='one'))
    lst.append(Category.objects.create(name='two'))
    lst.append(Category.objects.create(name='three'))
    lst.append(Category.objects.create(name='four'))
    return lst


@pytest.fixture()
def author_fixture():
    lst = []
    lst.append(Author.objects.create(first_name='Darek', last_name='Nowak', birth_date=datetime(2000, 10, 10)))
    lst.append(Author.objects.create(first_name='Janek', last_name='Kowalski', birth_date=datetime(1999, 5, 12)))
    return lst


@pytest.fixture()
def book_fixture(publishers_fixture, categories_fixture, author_fixture):
    book = Book.objects.create(
        author=author_fixture[0],
        publisher=publishers_fixture[0],
        title='test_title',
        year=2000,
    )
    book.categories.set(categories_fixture)
    return book


@pytest.fixture()
def user_fixture():
    user = User.objects.create(username='dawid')
    return user


@pytest.fixture()
def user_with_view_book_perm_fixture():
    user = User.objects.create(username='dawid')
    perm = Permission.objects.get(codename='view_book')
    user.user_permissions.add(perm)
    return user


@pytest.fixture()
def user_with_view_category_perm_fixture():
    user = User.objects.create(username='dawid')
    perm = Permission.objects.get(codename='view_category')
    user.user_permissions.add(perm)
    return user
