from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer


# 🔐 Seller permission
class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        # 👇 create/update/delete सिर्फ seller
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsSeller()]
        # 👇 बाकी सब login user देख सकते हैं
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)