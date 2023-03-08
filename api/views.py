from django.shortcuts import render
from .modules.brands.models import Brand


def index(request):
    """
    View function for homepage
    """
    brands_amount = Brand.objects.all().count()

    return render(
        request,
        'index.html',
        context={'brands_amount': brands_amount})
