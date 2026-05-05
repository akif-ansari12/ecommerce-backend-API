from django.db import models
from orders.models import Order
from accounts.models import User


class Payment(models.Model):
   
    PAYMENT_STATUS = (
      ('pending', 'Pending'),
      ('success', 'Success'),
      ('failed', 'Failed'),
   )


    PAYMENT_METHOD = (
       ('razorpay', 'Razorpay'),
        ('stripe', 'Stripe'),
        ('cod', 'Cash on Delivery'),
   )


    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.FloatField()

    Payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='razopay')
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')

    transaction_id = models.CharField(max_length=100, blank=True, null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"