from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from items.models import Item, ItemImage


class ItemCreateView(CreateView):
    pass
#
#    model = Item
#
#    fields = [
#        'title',
#        'content',
#        'image',
#        ]
#
#    template_name = "items/item_create.html"
#
#    def form_valid(self, form):
#
#        form.instance.user = self.request.user
#
#        return super(ItemCreateView, self).form_valid(form)


@login_required
def new_item(request):

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        # from IPython import embed; embed()
        content_images = request.FILES.getlist('content_images')

        # from IPython import embed; embed()
        item = Item.objects.create(
            user=request.user,
            title=title,
            content=content,
            image=image,
        )

        for i, files in enumerate(content_images):
            ItemImage.objects.create(
               item=item,
               image=files,
               )

        return redirect(
            reverse(
                "itemdetail",
                kwargs={
                    "slug": item.hash_id,
                    }
            )
        )

    return render(
        request,
        "items/item_create.html",
        context={}
    )
