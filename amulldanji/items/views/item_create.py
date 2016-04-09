from django.views.generic import CreateView
from items.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemCreateView(LoginRequiredMixin, CreateView):

    model = Item

    fields = [
        'title',
        'content',
        'image',
        ]

    template_name = "items/item_create.html"

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super(ItemCreateView, self).form_valid(form)
