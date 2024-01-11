from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from products.models import *


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        products_set = Product.objects.filter(category_id=category_id)
    else:
        products_set = Product.objects.all()
    products_set.order_by('id')

    paginator = Paginator(products_set, per_page=3)
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': page,
        'page_numbers': paginator.get_elided_page_range(page_number, on_each_side=2, on_ends=0),
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
