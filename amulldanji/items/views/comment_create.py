from django.views.generic import CreateView
from django.shortcuts import redirect
from items.models import Comment, Item
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentCreateView(LoginRequiredMixin, CreateView):

    model = Comment

    fields = [
            'content',
            ]

    def form_valid(self, form):
        # User
        form.instance.user = self.request.user

        # Item
        form.instance.item = Item.objects.get(
            hash_id=self.kwargs.get('slug'),
        )
        return super(CommentCreateView, self).form_valid(form)
