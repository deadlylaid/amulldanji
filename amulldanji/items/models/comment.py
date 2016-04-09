from django.db import models
from users.models import User
from items.models import Item
from django.core.urlresolvers import reverse


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

    def get_absolute_url(self):
        return reverse(
            "itemdetail",
            kwargs={
                "slug": self.item.hash_id,
            }
        )
