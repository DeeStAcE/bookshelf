import pytest
from django.test import TestCase
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_main():
    client = Client()
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200
