from django.conf.urls import url
from django.contrib import admin

from amulldanji.views import HomeView
from users.views import *
from items.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^joinus', JoinusView.as_view(), name='joinus'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'),

    url(r'^itemlist', ItemListView.as_view(), name='itemlist'),
]
