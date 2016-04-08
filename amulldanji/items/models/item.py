from django.db import models
from users.models import User


class Item(models.Model):

    user = models.ForeignKey(
            User,
            )

    image = models.ImageField(
            null=True,
            blank=True,
            )

    title = models.CharField(
            max_length=50,
            )

    content = models.TextField()

    created_at = models.DateTimeField(
            auto_now_add=True,
            )

    def __str__(self):
        return self.title
