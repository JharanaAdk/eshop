from django.shortcuts import render, redirect
from account.models import Order, OrderItem

def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, "product/order.html", context)

def vieworder(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems= OrderItem.objects.filter(order=order)
    context = {'order': order, 'orderitems':orderitems}
    return render(request, "product/orderview.html", context)