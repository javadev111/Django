from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    title = 'Products'

    products_list = Product.objects.all()[:4]

    content = {'title': title, 'products': products_list}
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
