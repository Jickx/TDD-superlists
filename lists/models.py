from django.db import models


class Item(models.Model):
    objects = None
    text = models.TextField()
