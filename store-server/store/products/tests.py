from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):
    def test_index(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsViewTestCase(TestCase):
    fixtures = [
        'categories.json',
        'products.json',
    ]

    def _common_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_first_page(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_test(response)
        self.assertQuerysetEqual(
            Product.objects.all().order_by('id')[:3],
            response.context_data['object_list'],
        )

    def test_first_page_with_category(self):
        category_id = 3  # Обувь (1 товар)
        path = reverse('products:category', kwargs={'category_id': category_id})
        response = self.client.get(path)

        self._common_test(response)
        self.assertQuerysetEqual(
            Product.objects.filter(category_id=category_id).order_by('id')[:3],
            response.context_data['object_list'],
        )
