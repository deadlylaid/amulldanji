from django.views.generic import DetailView
from items.models import Item


class ItemDeatilView(DetailView):

    model = Item

    template_name = "items/detail.html"
    object_context_name = "item"
    slug_field = "hash_id"
