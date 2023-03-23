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


def store(request):
    data = Product.objects.raw('SELECT * FROM main_product')
    return render(request, 'main/temp_shop_items.html', context={'data': data})


def product_detail(request, pk):
    prod = Product.objects.get(id=pk)
    return render(request, 'main/product.html', context={'prod': prod})

def laptop_store(request):
    data = Product.objects.raw(
        'SELECT main_product.id, main_product.image_url, main_product.name, main_product.price, main_productcategory.name '
        'FROM main_product '
        'INNER JOIN main_productcategory ON main_product.category_id = main_productcategory.id '
        'WHERE main_productcategory.id=1')
    return render(request, 'main/temp_shop_items.html', context={'data': data})

