from django.urls import path
from .views import customer_dashboard

urlpatterns = [
    path('customer/dashboard/', customer_dashboard, name='customer-dashboard'),
]