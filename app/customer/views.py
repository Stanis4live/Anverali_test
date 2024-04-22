from django.shortcuts import render, redirect
from django.db import transaction
from .forms import EditCustomerForm
from .models import Order


def customer_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = EditCustomerForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer-dashboard')
    else:
        form = EditCustomerForm(instance=request.user)

    return render(request, 'customer-dashboard.html', {
        'form': form,
        'user': request.user
    })


@transaction.atomic
def add_order(request):
    if request.method == 'POST':
        new_order = Order()
        new_order.save()
        user = request.user
        user.experience += 1
        user.save()
        return redirect('customer-dashboard')
