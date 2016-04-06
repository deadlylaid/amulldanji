from django.views.generic import View
from django.shortcuts import render


class JoinusView(View):

    def get(self, request):
        return render(
                request,
                "users/joinus.html",
                context={}
                )
