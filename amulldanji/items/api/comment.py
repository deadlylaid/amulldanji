from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers

from items.models import Item, Comment

import json


class CommentListApiView(APIView):

    def get(self, request, **kwargs):

        item = Item.objects.get(hash_id=kwargs.get('slug'))

        data = [
                comment.send_object_dic
                for comment in item.comment_set.all()
            ]
        return Response(
                data
        )

    def post(self, request, **kwargs):

        item = Item.objects.get(hash_id=kwargs.get('slug'))

        comment = item.comment_set.create(
                user=request.user,
                content=request.POST.get('comment'),
                )

        user_id = {}
        user_id['user_id'] = comment.user.username

        # json.dump must receive dictionary type
        return Response(
            data={
                'comment_id': json.dumps(user_id),
            },
            status=201,
            )
