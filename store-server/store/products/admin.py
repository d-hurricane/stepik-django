from django.contrib import admin

import products.models as products


admin.site.register(products.ProductCategory)
admin.site.register(products.Product)
