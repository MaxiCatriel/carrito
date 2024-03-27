from django.shortcuts import render, HttpResponse, redirect
from CarritoApp.models import Producto 
from CarritoApp.Carrito import Carrito



# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    print(productos)  
       # Calcular el total del carrito
    carrito = Carrito(request)
    total_carrito = carrito.obtener_total()

    return render(request, 'tienda.html', {'productos': productos, 'total_carrito': total_carrito})
    

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")
