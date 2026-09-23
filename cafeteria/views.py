import json
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ContactoForm

def inicio(request):
    return render(request, 'cafeteria/index.html')

def menu(request):
    # CORREGIDO: Aquí debe leer productos.json de la raíz
    archivo = Path(settings.BASE_DIR) / 'data' / 'productos.json'

    with open(archivo, 'r', encoding='utf-8') as archivo_json:
        productos = json.load(archivo_json)

    return render(
        request,
        'cafeteria/menu.html',
        {
            'productos': productos
        }
    )
    
def nosotros(request):
    return render(request, 'cafeteria/nosotros.html')

def noticias(request):
    # CORREGIDO: Aquí lee noticias.json de la raíz sin la palabra 'cafeteria'
    archivo = Path(settings.BASE_DIR) / 'data' / 'noticias.json'

    with open(archivo, 'r', encoding='utf-8') as archivo_json:
        lista_noticias = json.load(archivo_json)

    lista_noticias = sorted(
        lista_noticias,
        key=lambda noticia: noticia['fecha'],
        reverse=True
    )

    return render(
        request,
        'cafeteria/noticias.html',
        {
            'noticias': lista_noticias
        }
    )

def contacto(request):

    if request.method == 'POST':

        formulario = ContactoForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            return redirect('contacto_exito')

    else:

        formulario = ContactoForm()

    return render(
        request,
        'cafeteria/contacto.html',
        {
            'formulario': formulario
        }
    )


def contacto_exito(request):

    return render(
        request,
        'cafeteria/contacto_exito.html'
    )