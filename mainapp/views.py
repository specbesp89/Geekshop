from django.shortcuts import render
import datetime
from mainapp.models import ProductCategory,Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def index(request):

    context = {
        'title':'Главная страница'
    }
    return render(request, 'mainapp/index.html', context)

#
# def products(request, category_id=None):
#     context = {
#         'title': 'Наша продукция',
#         'categories': ProductCategory.objects.all()
#     }
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#     context.update({'products': products})
#
#     return render(request, 'mainapp/products.html', context)



def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(object_list=products.order_by('-price'), per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(page)

    context = {
            'title': 'Наша продукция',
            'categories': ProductCategory.objects.all(),
            'products': products_paginator
        }
    return render(request, 'mainapp/products.html', context)

