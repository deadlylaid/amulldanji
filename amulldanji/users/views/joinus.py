from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


class JoinusView(View):

    def get(self, request):
        return render(
                request,
                "users/joinus.html",
                context={}
                )

    def post(self, request):

        received_id = request.POST.get("id")
        received_pw = request.POST.get("pw")

        user = get_user_model().objects.create_user(
                username=received_id,
                password=received_pw,
                )
        user = authenticate(
                username=received_id,
                password=received_pw,
                )

        login(request, user)

        return redirect(reverse("home"))
