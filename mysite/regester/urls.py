from django.urls import path
from .views import *

urlpatterns = [
    path('regester/', regester, name='regester'),
    path('login/', login, name='login')
]