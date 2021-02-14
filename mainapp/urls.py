from django.urls import path

import mainapp.views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp_views.products, name='index'),
   path('<int:category_id>/', mainapp_views.products, name='category'),
   path('page/<int:page>/', mainapp_views.products, name='page'),
]
