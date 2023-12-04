from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from django.db.models import Max, Min


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product-list.html', {'products': products})


def product_detail(request):
    products = Product.objects.all()
    return render(request, 'product-detail.html', {'products': products})


def wishlist(request):
    return render(request, 'wishlist.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def my_account(request):
    return render(request, 'my-account.html')


