from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import Order, OrderItem

# Create your views here.

@login_required
def orders_list(request):
    orders =Order.objects.filter(user = request.user)
    return render(request,'orders/orders-list.html',{ 'orders': orders })
    