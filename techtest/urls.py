"""techtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from techtest.articles.views import ArticleAPIView, ArticleEditAPIView
from techtest.regions.views import RegionAPIView, RegionEditAPIView
from techtest.authors.views import AuthorAPIView, AuthorEditAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", ArticleAPIView.as_view(), name="articles-list"),
    path("articles/<int:id>/", ArticleEditAPIView.as_view(), name="article"),
    path("regions/", RegionAPIView.as_view(), name="regions-list"),
    path("regions/<int:id>/", RegionEditAPIView.as_view(), name="region"),
    path("author/", AuthorAPIView.as_view(), name='author'),
    path("author/<int:id>/", AuthorEditAPIView.as_view(), name="author_modify"),
]
