from django.shortcuts import render
import datetime
from mainapp.models import ProductCategory,Product



# Create your views here.
def index(request):

    context = {
        'title':'Главная страница'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)


    context = {
        'title': 'Наша продукция',

        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()


    }

    return render(request, 'mainapp/products.html', context)


