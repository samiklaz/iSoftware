from django.db import models


class Region(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    