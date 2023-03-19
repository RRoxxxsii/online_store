from django.urls import path
from .views import *

urlpatterns = [
    path('regester/', RegisterView.as_view(), name='regester'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout_user')
]