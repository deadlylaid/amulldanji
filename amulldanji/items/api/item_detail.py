from rest_framework.views import APIView
from rest_framework.response import Response

from items.models import Item, Comment


class ItemDetailApiView(APIView):

    def get(self, request, **kwargs):

        item = Item.objects.get(hash_id=kwargs.get('slug'))

        data = item.send_object_dic()

        data["comments"] = [
                comment.send_object_dic
                for comment in item.comment_set.all()
            ]
        return Response(
                data
                )
