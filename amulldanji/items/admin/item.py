from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'title',
        'content',

        'created_at',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'created_at',
    )
