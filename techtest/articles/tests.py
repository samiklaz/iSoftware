import imp
import json

from django.test import TestCase
from django.urls import reverse

from techtest.articles.models import Article
from techtest.regions.models import Region


class ArticleListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("articles-list")
        self.article_1 = Article.objects.create(title="Fake Article 1")
        self.region_1 = Region.objects.create(code="AL", name="Albania")
        self.region_2 = Region.objects.create(code="UK", name="United Kingdom")
        self.article_2 = Article.objects.create(
            title="Fake Article 2", content="Lorem Ipsum"
        )
        self.article_2.regions.set([self.region_1, self.region_2])

    import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from techtest.regions.models import Region
from techtest.authors.models import Author
from django.urls import path
from techtest.articles.models import Article
from techtest.articles.serializers import ArticleSerializer
from techtest.articles.views import *


class ArticleTestCase(APITestCase):
    urlpatterns = [
        path("articles/", ArticleAPIView.as_view(), name="articles-list"),
        path("articles/<int:id>/", ArticleEditAPIView.as_view(), name="article"),
    ]

    def test_authors_get_all(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_create(self):
        url = reverse('articles-list')
        data =  {
            "title": "The birth of a King",
            "content": "A King was  born on this day",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_author_get_single(self):
        response = self.client.get('/articles/', {'id': 1})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)