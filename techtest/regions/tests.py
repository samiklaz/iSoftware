import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from techtest.regions.serializers import RegionSerializer
from techtest.regions.models import Region
from techtest.authors.models import Author
from django.urls import path

from techtest.articles.views import ArticleAPIView, ArticleEditAPIView
from techtest.regions.views import RegionAPIView, RegionEditAPIView
from techtest.authors.views import AuthorAPIView, AuthorEditAPIView


class RegionTestCase(APITestCase):
    urlpatterns = [
        path("regions/", RegionAPIView.as_view(), name="regions-list"),
        path("regions/<int:id>/", RegionEditAPIView.as_view(), name="region"),
    ]

    def test_region_get_all(self):
        url = reverse('regions-list')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_region_create(self):
        url = reverse('regions-list')
        data = {
            "code": "NG",
            "name": "Nigeria"
        } 

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Region.objects.count(), 1)
        self.assertEqual(Region.objects.get().name, 'Nigeria')
        self.assertEqual(Region.objects.get().code, 'NG')


    def test_region_get_single(self):
        response = self.client.get('/regions/', {'id': 1})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    


    