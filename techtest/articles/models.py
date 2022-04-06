from django.db import models
from techtest.authors.models import Author
from techtest.regions.models import Region

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True, null=True
    )

    def __str__(self):
        return self.title