from django.shortcuts import render
from .models import *
import functools
from django.core.paginator import Paginator

def index(request):
    return render(request, 'main/index.html')


def store(request):
    data = Product.objects.raw('SELECT * FROM main_product')
    return render(request, 'main/temp_shop_items.html', context={'data': data})


def shop_detail(request, pk):
    prod = Product.objects.get(id=pk)
    return render(request, 'main/product.html', context={'prod': prod})


def checkout(request):
    return render(request, 'main/checkout.html')


# id=1- Ноутбуки id=2-Телефоны id=3-Наушники
def store_category(cat_id):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request):
            data = Product.objects.filter(category__id=cat_id).values('id', 'image_url', 'name', 'price',
                                                                      'category__name')
            return func(request, data)
        return wrapper
    return decorator


@store_category(cat_id=1)
def laptop_store(request, data):

    return render(request, 'main/temp_shop_items.html', context={'data': data})


@store_category(cat_id=2)
def mobile_store(request, data):
    return render(request, 'main/temp_shop_items.html', context={'data': data})


@store_category(cat_id=3)
def headphones_store(request, data):
    return render(request, 'main/temp_shop_items.html', context={'data': data})
