from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction
from .forms import EditPerformerForm
from customer.models import Order


@transaction.atomic
def performer_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = EditPerformerForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('performer-dashboard')
    else:
        form = EditPerformerForm(instance=request.user)
    free_orders_count = Order.objects.count()
    return render(request, 'performer-dashboard.html', {
        'form': form,
        'user': request.user,
        'free_orders_count': free_orders_count
    })


@transaction.atomic
def execute_order(request):
    if request.method == 'POST':
        order_to_delete = Order.objects.first()
        if order_to_delete:
            order_to_delete.delete()
            user = request.user
            user.experience += 1
            user.save()
        return redirect('performer-dashboard')