from django.contrib import admin

import products.models as products


@admin.register(products.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class PriceListFilter(admin.SimpleListFilter):
    title = 'price'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('0', 'free'),
            ('1', 'cheaply (up to 5 000 RUB)'),
            ('2', 'expensive (over 5 000 RUB)'),
        )

    def queryset(self, request, queryset):
        match self.value():
            case '0': return queryset.filter(price=0)
            case '1': return queryset.filter(price__gt=0, price__lte=5000)
            case '2': return queryset.filter(price__gt=5000)
            case _: return queryset


@admin.register(products.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'view_price')
    list_filter = ('category', PriceListFilter)
    ordering = ('name', )

    @admin.display(description='price')
    def view_price(self, obj):
        return f'{obj.price:15,.2f},RUB'.replace(',', '\xA0')
