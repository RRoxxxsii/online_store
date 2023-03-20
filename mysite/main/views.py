from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def store(request):
    return render(request, 'main/store.html')


def checkout(request):
    return render(request, 'main/checkout.html')


def product(request):
    return render(request, 'main/product.html')
