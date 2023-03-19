from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def store(request):
    return render(request, 'main/store.html')


def checkout(requets):
    return render(requets, 'main/checkout.html')


