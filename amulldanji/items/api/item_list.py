from rest_framework.views import APIView
from rest_framework.response import Response

from items.models import Item


class ItemListApiView(APIView):
    def get(self, request):

        items = Item.objects.all()

        data = [
            item.send_click_point()
            for item in items
        ]
        return Response(
                data
                )
