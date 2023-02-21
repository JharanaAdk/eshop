from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from products.models import *
from account.models import *
import random
from django.contrib.auth.models import User

@login_required(login_url='loginpage')
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    # cart item for checkout function
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    #totaling the price of all cart items
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty
    userprofile = Profile.objects.filter(user=request.user).first()
    context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile}
    return render(request, 'product/checkout.html', context)



def placeorder(request):
    if request.method == 'POST':
        #first authenticate the filter the user data 
        currentuser = User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()
        # Profile information form to save all the credientials and basic details of user
        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.country = request.POST.get('country')
            userprofile.state = request.POST.get('state')
            userprofile.city = request.POST.get('city')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.address = request.POST.get('address')
            userprofile.save()
        # neworder place form to save all the credientials and basic details of user
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.country = request.POST.get('country')
        neworder.state = request.POST.get('state')
        neworder.city = request.POST.get('city')
        neworder.pincode = request.POST.get('pincode')
        neworder.address = request.POST.get('address')

        neworder.payment_mode = request.POST.get('payment_mode')

        #viewing the cart item and total price of user shopping
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price *item.product_qty
        
        #generating the unique tracking no of each and every order of user
        neworder.total_price = cart_total_price
        trackno = 'eshop'+str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no = trackno) is None:
            trackno = 'eshop'+str(random.randint(1111111, 9999999))
        
        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity = item.product_qty
            )
        #to decrease the product quantity from the available stock
        orderproduct = Product.objects.filter(id=item.product_id).first()
        orderproduct.quantity = orderproduct.quantity - item.product_qty
        orderproduct.save()

        # to clear the user cart once user place the order
        Cart.objects.filter(user=request.user).delete()
        messages.success(request, "your order has been placed sucessfully")
        return redirect('/')

            