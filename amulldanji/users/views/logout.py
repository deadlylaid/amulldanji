from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, get_user_model
from django.core.urlresolvers import reverse


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse("home"))
