from django.shortcuts import render, redirect

from .forms import ClienteForm, ProductoForm
from .models import Cliente, Producto

# Create your views here.
def indexd(request):
    return render (request, 'indexd.html')

def QuienesSomos(request):
    return render (request, 'QuienesSomos.html')

def contacto(request):
    return render (request, 'contacto.html')

def galeria(request):
    return render (request, 'galeria.html')

def peliculasAPI(request):
    return render (request, 'peliculasAPI.html')

def formularioRegistro(request):
    return render (request, 'formularioRegistro.html')

def listadocli(request):
    clientes = Cliente.objects.all()
    datos = {
        'clientes':clientes
    }
    return render (request, 'listadocli.html' , datos)

def listadoproduc(request):
    productos = Producto.objects.all()
    datos = {
        'productos':productos
    }
    return render (request, 'listadoproduc.html' , datos)

def formcliente(request):
    datos = {
        'form': ClienteForm()
    }
    if request.method=='POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="guardados correctamente"
    return render (request, 'formcliente.html', datos)

def formproducto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method=='POST':
        formulario=ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="guardados correctamente"
    return render (request, 'formproducto.html', datos)

def formmodcliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    datos={
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario=ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect ('listadocli')

    return render(request, 'formmodcliente.html', datos)

def formmodproducto(request,id):
    producto = Producto.objects.get(codigo=id)
    datos={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect ('listadoproduc')

    return render(request, 'formmodproducto.html', datos)

def formdelcliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect ('listadocli')

def formdelproducto(request, id):
    producto = Producto.objects.get(codigo=id)
    producto.delete()
    return redirect ('listadoproduc')

    