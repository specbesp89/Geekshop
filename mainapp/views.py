from django.shortcuts import render
import datetime
import json



# Create your views here.
def index(request):

    context = {
        'title':'Главная страница'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):


    context = {
        'title': 'Наша продукция',

        'products': [
            {
                'name': 'FENDER PLAYER TELE HH MN TPL',
                'price': 154000,
                'src': 'vendor/img/products/FENDER-PLAYER.jpg',
                'description': 'Эта гитара станет хорошим приобретением для гитаристов, которые ищут не только премиальный фендеровский звук, но и шикарный стиль электрогитар Fender.'

            },
            {
                'name': 'FENDER American Ultra Stratocaster®, Maple Fingerboard, Texas Tea',
                'price': 200000,
                'src': 'vendor/img/products/FENDER_American.jpg',
                'description': 'Для искушенных музыкантов, которые хотят получить лучшее из возможного с точки зрения звука, гибкости настроек, точности и производительности'

            },
            {
                'name': 'GIBSON Les Paul Standard 60s Bourbon Burst',
                'price': 238000,
                'src': 'vendor/img/products/LesPaul_Standard 60s.jpg',
                'description': 'профессиональная шестиструнная электрогитара, переиздание легендарной модели Les Paul Standard 1960 года.'

            },
            {
                'name': 'JACKSON USA Signature David Ellefson Concert™ Bass CB V, Ebony Fingerboard, Satin Black',
                'price': 515000,
                'src': 'vendor/img/products/JACKSON_BASS.jpg',
                'description': 'Профессиональный именной инструмент David Ellefson из группы Megadeth.'

            },
            {
                'name': 'FENDER Acoustasonic Stratocaster Black',
                'price': 253000,
                'src': 'vendor/img/products/FENDER_Acoustasonic.jpg',
                'description': 'Объемный чистый звук гарантирован.'

            },
            {
                'name': 'GIBSON 2019 THUNDERBIRD BASS EBONY',
                'price': 209000,
                'src': 'vendor/img/products/GIBSON_BASS.jpg',
                'description': 'Четырехструнная бас-гитара модельного ряда 2019 года, сохранившая характерные черты, выделяющие этот инструмент среди других с момента его появления в 1963 году.'

            },],

    }

    return render(request, 'mainapp/products.html', context)


