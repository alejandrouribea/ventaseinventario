from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def productos(request):
    return render(request, "productos.html")

def ventas(request):
    return render(request, "ventas.html")

def barra(request):
    return render(request, "navbar.html")

def crearProducto(request):
    return render(request, "crearProducto.html")