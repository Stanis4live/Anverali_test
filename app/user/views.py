from django.shortcuts import render
from customer.models import Order


def home(request):
    free_orders_count = Order.objects.count()
    return render(request, 'home.html', {'free_orders_count': free_orders_count})
