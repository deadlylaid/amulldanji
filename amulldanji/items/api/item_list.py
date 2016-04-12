from django.views.generic import View
from django.http import HttpResponse


class ItemListApiView(View):

    def get(self, request):

        return HttpResponse(
            "hello world",
            )
