from django.shortcuts import render
from django.views.generic import DetailView
from .models import *


def index(request):
    return render(request, 'main/index.html')


def store(request):
    data = Product.objects.raw('SELECT * FROM main_product')

    return render(request, 'main/temp_shop_items.html', context={'data': data})


def product_detail(request, pk):
    prod = Product.objects.get(id=pk)
    return render(request, 'main/product.html', context={'prod': prod})


def checkout(request):
    return render(request, 'main/checkout.html')




