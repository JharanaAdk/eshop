from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product, Wishlist

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request, 'product/wishlist.html', context)
