from django.urls import path
from .views import place_order, order_history, order_detail

urlpatterns = [
    path('place/', place_order),
    path('history/', order_history),
    path('<int:order_id>/', order_detail),
]