from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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


@login_required
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


@login_required
def basket_remove(request, basket_id):
    basket_item = Basket.objects.filter(id=basket_id, user=request.user).first()
    if basket_item is not None:
        basket_item.delete()
    return redirect(to=request.META['HTTP_REFERER'])
