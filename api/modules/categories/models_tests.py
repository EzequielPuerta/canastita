from django.test import TestCase
from .models import Category


class CategoryTestCase(TestCase):

    def test_category_creation(self):
        category_name = "Almacen"
        category = Category.objects.create(name=category_name)
        self.assertEqual(category.name, category_name)
