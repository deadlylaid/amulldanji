from django.views.generic import View
from django.http import HttpResponse

import json

from items.models import Item


class ItemListApiView(View):
    def get(self, request):

        items = Item.objects.all()

        data = [

            item.send_object_dic()
            for item in items
        ]

        return HttpResponse(
            json.dumps(data),
            content_type="application/json",
            )
