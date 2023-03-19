from django.shortcuts import render

def login(request):
    return render(request, 'regester/login.html')


def regester(request):
    return render(request, 'regester/regester.html')


