from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    phone = models.CharField(
            null=True,
            blank=True,
            max_length=11,
            )

    address = models.CharField(
            max_length=30,
            null=True,
            blank=True,
            )
    ticket = models.IntegerField(default=0)
