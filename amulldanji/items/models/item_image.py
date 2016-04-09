from django.db import models
from django.contrib import admin
from .item import Item


class ItemImage(models.Model):

    item = models.ForeignKey(
        Item,
        related_name="images",
        )
    image = models.ImageField(
        blank=True,
        null=True,
        )
