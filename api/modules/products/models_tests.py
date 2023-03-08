from django.test import TestCase
from .models import Product
from ..brands.models import Brand
from ..categories.models import Category


class ProductTestCase(TestCase):

    def test_product_creation(self):
        brand_name = "Marolio"
        brand = Brand.objects.create(name=brand_name)

        category_name = "Almacen"
        category = Category.objects.create(name=category_name)

        product_name = "Arroz"
        product = Product.objects.create(name=product_name, brand=brand)
        self.assertEqual(product.name, product_name)
        self.assertEqual(product.brand, brand)
        self.assertEqual(len(product.categories.all()), 0)
        product.categories.add(category)
        self.assertEqual(len(product.categories.all()), 1)
        self.assertIn(category, product.categories.all())
