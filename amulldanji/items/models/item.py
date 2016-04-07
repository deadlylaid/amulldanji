from django.db import models
from users.models import User


class Item(models.Model):

    user = models.ForeignKey(
            User,
            related_name='items',
            )


    title = models.CharField(
            max_length=50,
            )

    created_time = models.DateTimeField(
            auto_now_add=True,
            )


    content = models.TextField()

    def __str__(self):
        return self.title
