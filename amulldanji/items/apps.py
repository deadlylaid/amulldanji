from django.apps import AppConfig


class ItemsAppConfig(AppConfig):
    name = "items"

    def ready(self):
        from items.signals.post_save import insert_hash_id
