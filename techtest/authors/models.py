from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        names = str(self.first_name) + " " + str(self.last_name)
        return names

    def __str__(self):
        return self.full_name()
