# Item, Comment 테이블 만든후 제작
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class MyPageView(LoginRequiredMixin, DetailView):

    template_name = "users/mypage.html"

    def get_object(self):
        return self.request.user
