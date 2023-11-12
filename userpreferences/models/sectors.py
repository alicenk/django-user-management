from django.db import models


class Sector(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
