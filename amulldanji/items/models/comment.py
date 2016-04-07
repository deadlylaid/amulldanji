from django.db import models
from users.models import User
from items.models import Item


class Comment(models.Model):

    user = models.ForeignKey(
        User,
        )

    item = models.ForeignKey(
        "Item",
        )

    content = models.TextField()

    def __str__(self):
        return self.content
