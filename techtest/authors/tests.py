import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from techtest.regions.serializers import RegionSerializer
from techtest.regions.models import Region
from techtest.authors.models import Author
from django.urls import path
from techtest.authors.views import AuthorAPIView, AuthorEditAPIView


class AuthorTestCase(APITestCase):
    urlpatterns = [
        path("author/", AuthorAPIView.as_view(), name='author'),
    ]
    def test_authors_get_all(self):
        url = reverse('author')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_create(self):
        url = reverse('author')
        data = {
            "first_name": "Samuel",
            "last_name": "Asuquo"
        } 

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().first_name, 'Samuel')
        self.assertEqual(Author.objects.get().last_name, 'Asuquo')

    def test_region_get_single(self):
        response = self.client.get('/author/', {'id': 1})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)