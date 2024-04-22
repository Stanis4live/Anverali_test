from django.urls import path
from .views import customer_dashboard, add_order

urlpatterns = [
    path('customer/dashboard/', customer_dashboard, name='customer-dashboard'),
    path('add-order', add_order, name='add-order'),
]