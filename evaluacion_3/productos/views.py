from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from productos.models import Productos



def inicio (request):
    return render(request,"index.html")

def login (request):
    return render(request,"login.html")

def seguimiento (request):
    return render(request,"seguimiento.html")

def contacto (request):
    return render(request,"contacto.html")

def formulario (request):
    return render(request,"formulario.html")

def carritodecompras (request):
    return render(request,"carritodecompras.html")

def productos (request):
    return render(request,"productos.html")

def administrador(request):
    productos = Productos.objects.all()
    #producto.imagenProd = request.FILE.get('txtImagen')

    datos = {
        'productos' : productos
            }
    return render(request, 'productos.html', datos )