from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    phone = models.CharField(
            max_langth=11
            )

    address = models.CharField(
            max_langth=30
            )
    ticket = models.IntegerField()
