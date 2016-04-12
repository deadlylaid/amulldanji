from django.conf.urls import url
from django.contrib import admin

from amulldanji.views import HomeView
from users.views import *
from items.views import *
from items.api import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ItemListView.as_view(), name='home'),

    url(r'^joinus/$', JoinusView.as_view(), name='joinus'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^mypage/(?P<pk>\d+)/$', MyPageView.as_view(), name='mypage'),

    url(r'^apilist/$', ItemListApiView.as_view(), name='itemapi'),
    url(r'^apidetail/$', ItemDetailApiView.as_view(), name='detailapi'),

    url(r'^itemcreate/$', new_item, name='newitem'),
    url(r'^item/(?P<slug>\w+)/$', ItemDeatilView.as_view(), name='itemdetail'),
    url(r'^item/(?P<slug>\w+)/comments/$', CommentCreateView.as_view(), name='item-comments'),
    url(r'^item/(?P<slug>\w+)/transfer/$', item_transfer, name='item_transfer'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
