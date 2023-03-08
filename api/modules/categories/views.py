from django.views import generic
from .models import Category


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'modules/categories/templates/category_list.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'modules/categories/templates/category_detail.html'
