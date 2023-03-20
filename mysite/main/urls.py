from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('store/', store, name='store'),
    path('checkout/', checkout, name='checkout'),
    path('product/', product, name='product'),
]