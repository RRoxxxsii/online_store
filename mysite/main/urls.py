from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('store/', store, name='store'),
    path('checkout/', checkout, name='checkout'),
    path('product/<int:product_id>/', shop_detail, name='product'),
    path('laptopstore/', laptop_store, name='laptop_store'),
    path('smartphones/', mobile_store, name='mobile_store'),
    path('headphones/', headphones_store, name='headphones_store')
]