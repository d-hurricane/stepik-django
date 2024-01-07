from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ProductCategory)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField()
