from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from .serializers import CartItemSerializer


# ➕ Add / Increase quantity
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    # 🔐 ensure authenticated (extra guard)
    if not request.user or request.user.is_anonymous:
        return Response({"error": "Authentication required"}, status=401)

    product_id = request.data.get('product_id')
    qty = int(request.data.get('quantity', 1))

    if not product_id:
        return Response({"error": "product_id required"}, status=400)

    product = get_object_or_404(Product, id=product_id)

    cart, _ = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        item.quantity = qty
    else:
        item.quantity += qty

    item.save()

    return Response({"msg": "added", "item_id": item.id, "quantity": item.quantity})


# 👀 View cart
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    if not request.user or request.user.is_anonymous:
        return Response({"error": "Authentication required"}, status=401)

    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    data = CartItemSerializer(items, many=True).data
    total = sum(i.product.price * i.quantity for i in items)

    return Response({"items": data, "total": total})


# ❌ Remove / Update quantity
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_item(request):
    if not request.user or request.user.is_anonymous:
        return Response({"error": "Authentication required"}, status=401)

    item_id = request.data.get('item_id')
    qty = int(request.data.get('quantity', 0))

    if not item_id:
        return Response({"error": "item_id required"}, status=400)

    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if qty <= 0:
        item.delete()
        return Response({"msg": "removed"})

    item.quantity = qty
    item.save()

    return Response({"msg": "updated", "quantity": item.quantity})