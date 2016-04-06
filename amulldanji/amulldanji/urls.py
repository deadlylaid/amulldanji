from django.conf.urls import url
from django.contrib import admin

from amulldanji.views import HomeView
from users.views import JoinusView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^joinus', JoinusView.as_view(), name='joinus'),

]
