from django.shortcuts import render, redirect
from products.models import *


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    values = {
        'user': request.user,
        'product': Product.objects.get(id=product_id),
    }
    basket_item = Basket.objects.filter(**values).first()
    if basket_item is None:
        basket_item = Basket(**values)
    basket_item.quantity += 1
    basket_item.save()
    return redirect(to=request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket_item = Basket.objects.get(id=basket_id)
    basket_item.delete()
    return redirect(to=request.META['HTTP_REFERER'])
