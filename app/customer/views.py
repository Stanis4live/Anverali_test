from django.shortcuts import render, redirect
from .forms import EditCustomerForm

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

