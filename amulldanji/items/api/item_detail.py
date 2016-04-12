from django.views.generic import View
from django.http import HttpResponse

import json

from items.models import Item, Comment


class ItemDetailApiView(View):

    def get(self, request):
        return HttpResponse(
            "helo",
            )
