from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.core.urlresolvers import reverse


class LoginView(View):
    def get(self, request):
        return render(
                request,
                "users/login.html",
                context={},
                )

    def post(self, request):

        received_id = request.POST.get("id")
        received_pw = request.POST.get("pw")
        # authenticate는 로그은 입력된 값이
        # 기존에 테이블에 존재하는 값과 일치하는지확인해줌
        user = authenticate(
            username=received_id,
            password=received_pw,
        )

        if user:
            login(request, user)
            return redirect(reverse("home"))
        return redirect(reverse("login"))
