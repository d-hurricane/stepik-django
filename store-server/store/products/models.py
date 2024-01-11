from django.db import models
from users.models import User


class ProductCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(item.sum() for item in self)

    def total_quantity(self):
        return sum(item.quantity for item in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'{self.user} | {self.product}'

    def sum(self):
        return self.product.price * self.quantity
