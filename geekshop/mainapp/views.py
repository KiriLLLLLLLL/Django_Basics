from django.shortcuts import render

from mainapp.models import Product, CategoryMenu


def index(request):

    title = 'каталог'

    #

    products = Product.objects.all()[:4]

    category_menu = CategoryMenu.objects.all()

    context = {
        'title': title,
        #'links_menu': links_menu,
        'related_products': products,
        'category_menu': category_menu
    }

    return render(request, 'mainapp/products.html', context)
