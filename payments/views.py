import razorpay
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from orders.models import Order

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


# 🔥 Create Payment Order
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment(request):
    order_id = request.data.get('order_id')

    if not order_id:
        return Response({"error": "order_id required"}, status=400)

    order = Order.objects.get(id=order_id, user=request.user)

    amount = int(order.total_price * 100)  # paise

    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })

    return Response({
        "payment_id": payment['id'],
        "amount": amount
    })


# ✅ Verify Payment
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_payment(request):
    data = request.data

    try:
        client.utility.verify_payment_signature({
            'razorpay_order_id': data['razorpay_order_id'],
            'razorpay_payment_id': data['razorpay_payment_id'],
            'razorpay_signature': data['razorpay_signature']
        })

        return Response({"msg": "Payment Success"})
    except:
        return Response({"error": "Payment Failed"}, status=400)