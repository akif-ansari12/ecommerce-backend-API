from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404

from cart.models import Cart
from .models import Order, OrderItem


# 🔥 Place Order (cart → order)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic
def place_order(request):
    user = request.user

    # cart safe तरीके से लो
    cart, _ = Cart.objects.get_or_create(user=user)
    items = cart.items.select_related('product').all()

    if not items.exists():
        return Response({"error": "Cart is empty"}, status=400)

    total = 0

    # order create (initial 0)
    order = Order.objects.create(user=user, total_price=0)

    # items loop
    for item in items:
        price = item.product.price
        total += price * item.quantity

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=price
        )

    # total update
    order.total_price = total
    order.save()

    # cart empty
    items.delete()

    return Response({
        "msg": "Order placed",
        "order_id": order.id,
        "total": total
    })


# 📜 Order History (user के सभी orders)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')

    data = []
    for order in orders:
        items_data = []
        for item in order.items.all():
            items_data.append({
                "product": item.product.name,
                "quantity": item.quantity,
                "price": item.price
            })

        data.append({
            "order_id": order.id,
            "total": order.total_price,
            "items": items_data
        })

    return Response(data)


# 🔍 Single Order Detail (extra — interview bonus)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    items_data = []
    for item in order.items.all():
        items_data.append({
            "product": item.product.name,
            "quantity": item.quantity,
            "price": item.price
        })

    return Response({
        "order_id": order.id,
        "total": order.total_price,
        "items": items_data
    })