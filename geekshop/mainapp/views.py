from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, CategoryMenu


def products(request, pk=None):

    title = 'каталог'



    same_products = Product.objects.all()[:4]

    category_menu = CategoryMenu.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk <= 1:
            products =Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(CategoryMenu, pk=pk)
            products = Product.objects.filter(category_menu__pk=pk).order_by('price')

        context = {
            'title': title,
            'category_menu': category_menu,
            'category': category,
            'products': products,
            'related_products': same_products,
            'basket': basket,

        }
        return render(request, 'mainapp/products.html', context)

    products = Product.objects.all().order_by('price')

    context = {
        'title': title,
        'related_products': same_products,
        'category_menu': category_menu,
        'products': products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)
