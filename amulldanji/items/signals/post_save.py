from hashids import Hashids
from items.models import Item
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Item)
def insert_hash_id(sender, instance, created, **kwargs):
    if created:
        instance.get_hash_id()
