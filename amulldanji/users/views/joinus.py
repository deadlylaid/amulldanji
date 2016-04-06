from django.views.generic import View
from django.http import HttpResponse


class JoinusView(View):

    def get(self, request):
        return HttpResponse(
                "hello world",
                )
