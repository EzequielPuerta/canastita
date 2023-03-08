from django.contrib import admin
from .modules.brands.models import Brand
from .modules.categories.models import Category
from .modules.products.models import Product


class CategorizedItemAdmin(admin.ModelAdmin):
    def display_categories(self, brand):
        return ",".join((str(category) for category in brand.categories.all()))

    display_categories.short_description = Category._meta.verbose_name_plural


@admin.register(Brand)
class BrandAdmin(CategorizedItemAdmin):
    list_display = ('id', 'name', 'display_categories')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(CategorizedItemAdmin):
    list_display = ('id', 'name', 'brand', 'display_categories')
