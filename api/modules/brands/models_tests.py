from django.test import TestCase
from .models import Brand


class BrandTestCase(TestCase):

    def test_brand_creation(self):
        brand_name = "Marolio"
        brand = Brand.objects.create(name=brand_name)
        self.assertEqual(brand.name, brand_name)
