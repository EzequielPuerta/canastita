from django.views import generic
from .models import Brand


class BrandListView(generic.ListView):
    model = Brand
    template_name = 'modules/brands/templates/brand_list.html'


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = 'modules/brands/templates/brand_detail.html'
