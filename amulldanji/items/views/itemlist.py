from django.views.generic import ListView
from items.models import Item

class ItemListView(ListView):
    
    model = Item

    template_name = "items/list.html"
    context_object_name = "item_list"
