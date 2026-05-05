from django.urls import path
from .views import add_to_cart, view_cart, update_item

urlpatterns = [
    path('add/', add_to_cart),
    path('view/', view_cart),
    path('update/', update_item),
    
]