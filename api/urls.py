from django.urls import re_path
from . import views
from .modules.brands.views import BrandListView, BrandDetailView
from .modules.categories.views import CategoryListView, CategoryDetailView
from .modules.products.views import ProductListView, ProductDetailView

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^brands/$', BrandListView.as_view(), name='brands'),
    re_path(r'^brands/(?P<pk>\d+)$', BrandDetailView.as_view(), name='brand-detail'),
    re_path(r'^categories/$', CategoryListView.as_view(), name='categories'),
    re_path(r'^categories/(?P<pk>\d+)$', CategoryDetailView.as_view(), name='category-detail'),
    re_path(r'^products/$', ProductListView.as_view(), name='products'),
    re_path(r'^products/(?P<pk>\d+)$', ProductDetailView.as_view(), name='product-detail')]
