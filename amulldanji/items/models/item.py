from django.db import models
from users.models import User
from django.core.urlresolvers import reverse


class Item(models.Model):

    hash_id = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        unique=True,
    )

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

    def get_hash_id(self):
        from amulldanji.utils.hash_id import get_encoded_hash_id
        self.hash_id = get_encoded_hash_id(self)
        self.save()

    # DetailView, CreateView 사용시 redirect될 위치와 보낼 kwargs값
    def get_absolute_url(self):
            return reverse(
                "itemdetail",
                kwargs={
                    "pk": self.id,
                }
            )

    def __str__(self):
        return self.title
