from django.views import generic
from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'modules/products/templates/product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'modules/products/templates/product_detail.html'
