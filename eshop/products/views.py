from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def home(request):
    trending_product = Product.objects.filter(trending=1)
    context = {'trending_product': trending_product}
    return render(request, 'inc/index.html', context)

def catview(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'product/index.html', context)

def categoryproduct(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
       product= Product.objects.filter(category__slug= slug) 
       category = Category.objects.filter(slug=slug)
       context = {'product': product, 'category': category}
       return render(request, 'product/catprodview.html', context)
    else:
        messages.warning(request, 'invalid category')
        return redirect('catview')

def productview(request, cat_slug, prod_slug):
    if(Category.objects.filter(slug=cat_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            product = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'product': product}
            return render(request, 'product/prodview.html', context)
        else:
            messages.error(request, 'no such product')
            return redirect('categoryproduct')
    else:
        messages.error(request, ' No such category')
        return redirect('catview')
   

def productlistAjax(request):
    product = Product.objects.filter(status=0).values_list('name', flat=True)
    productlist = list(product)
    return JsonResponse(productlist, safe=False)

def searchproduct(request):
    if request.method == "POST":
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()
            if product:
                return redirect('product/'+product.category.slug+'/'+product.slug+'/')
            else:
                messages.info(request, "No such product found search relavant")
                return redirect(request.META.GET('HTTP_REFERER'))
    return redirect(request.META.GET('HTTP_REFERER'))

