from django.conf.urls import url
from django.contrib import admin

from amulldanji.views import HomeView
from users.views import *
from items.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^joinus', JoinusView.as_view(), name='joinus'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'),

    url(r'^itemlist', ItemListView.as_view(), name='itemlist'),
    url(r'^item/(?P<pk>\d+)/$', ItemDeatilView.as_view(), name='itemdetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
