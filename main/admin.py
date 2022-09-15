from django.contrib import admin

from .models import Item, Order, OrderItems


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
    )
    list_filter = (
        'name',
        'price',
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'creation_time',
        'comment',
        'total_cost',
        'discount',
    )
    list_filter = (
        'creation_time',
    )

    def total_cost(self, obj):
        return obj.get_cost()


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item',
        'order_id',
    )
    list_filter = (
        'order',
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
