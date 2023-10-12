from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Manufacturer, Product


def product_list(request, manufacturer_slug=None):
    manufacturer = None
    manufacturers = Manufacturer.objects.all()
    products = Product.objects.filter(available=True)
    if manufacturer_slug:
        manufacturer = get_object_or_404(Manufacturer, slug=manufacturer_slug)
        products = products.filter(manufacturer=manufacturer)
    return render(request, 'shop/product/list.html',
                  {'manufacturer': manufacturer,
                   'manufacturers': manufacturers,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})
