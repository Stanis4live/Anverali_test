from django.urls import path
from .views import performer_dashboard, execute_order

urlpatterns = [
    path('performer/dashboard/', performer_dashboard, name='performer-dashboard'),
    path('execute-order', execute_order, name='execute-order'),
]