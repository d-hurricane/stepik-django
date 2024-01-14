from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import ListView

from products.models import *


class IndexView(TemplateView):
    template_name = 'products/index.html'
    extra_context = {'title': 'Store'}


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3
    extra_context = {'title': 'Store - Каталог'}

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'category_id' in self.kwargs:
            queryset = queryset.filter(category_id=self.kwargs['category_id'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


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
