from django.db import models


def catalog_presentation(instance):
    result = str(instance.name)
    if result.isspace():
        result = '<>'
    code = str(instance.id) if instance.id else 'create'
    result = '{} ({})'.format(result, code)
    return result


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return catalog_presentation(self)


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return catalog_presentation(self)
