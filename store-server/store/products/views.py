from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic import ListView

from products.models import *


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'category_id' in self.kwargs:
            queryset = queryset.filter(category_id=self.kwargs['category_id'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.all()
        context['get_page_numbers'] = self.get_page_numbers
        return context

    def get_page_numbers(self):
        return []


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
