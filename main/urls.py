from django.urls import path
from .views import (item_view, create_checkout_session,
                    add_to_order, all_items_view)


urlpatterns = [
    path('', all_items_view),
    path('add_to_order/<item_id>', add_to_order),
    path('buy', create_checkout_session),
    path('item/<item_id>', item_view)
]
