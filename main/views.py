import stripe
from django.shortcuts import get_object_or_404, render

from .models import Item, Order


def all_items_view(request):
    items = Item.objects.all()
    return render(request, 'all_items.html', {'items': items})


def item_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_page.html', {'item': item})


def add_to_order(request, item_id):
    if not request.session.get('order_id'):
        order = Order.objects.create()
        request.session['order_id'] = order.id
    else:
        order = Order.objects.get(id=request.session['order_id'])
    item = get_object_or_404(Item, id=item_id)
    order.items.add(item)
    cost = order.get_cost()
    context = {
        'items': order.items.all(),
        'order': True,
        'cost': cost
    }
    return render(request, 'all_items.html', context)


def create_checkout_session(request):
    order = get_object_or_404(
        Order,
        id=request.session['order_id']
    )
    line_items = []
    for item in order.items.all():
        line_items.append({
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
            'discount': order.discount
        })
    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='templates/success.html',
        cancel_url='templates/cancel.html',
    )
    return session.id
