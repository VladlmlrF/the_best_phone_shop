from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:manufacturer_slug>/', product_list, name='product_list_by_manufacturer'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]