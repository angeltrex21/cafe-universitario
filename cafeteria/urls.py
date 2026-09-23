
from django.urls import path

from . import views


urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('menu/', views.menu, name='menu'),

    path('nosotros/', views.nosotros, name='nosotros'),

    path('noticias/', views.noticias, name='noticias'),

    path('contacto/', views.contacto, name='contacto'),

    path(
        'contacto/exito/',
        views.contacto_exito,
        name='contacto_exito'
    ),

]
