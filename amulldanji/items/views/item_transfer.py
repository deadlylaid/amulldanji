from django.contrib.auth.decorators import login_required
from items.models import Item, User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


@login_required
def item_transfer(request, slug):

    item = Item.objects.get(hash_id=slug)

    item.user.ticket += 1
    item.user.save()

    if request.user.ticket > 0:
        request.user.ticket -= 1
        request.user.save()

        item.delete()
        # instance delete => DB yes
        # item.is_sold_out = True

    return redirect(
        reverse(
            'home'
        )
    )
