from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login(request):
    return render(request, 'regester/login.html')


def regester(request):
    return render(request, 'regester/regester.html')


def logout_user(request):
    logout(request)
    return redirect('index')


