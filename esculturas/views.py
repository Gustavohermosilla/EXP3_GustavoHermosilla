from django.shortcuts import render, redirect
from .models import *
from .forms import EsculturasForm, RegistroUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def principal(request):
    return render(request, 'principal.html')

def productos(request):
    return render(request, 'productos.html')

def quiensomos(request):
    return render (request, 'quiensomos.html')
def feriados(request):
    return render (request, 'feriados.html')

@login_required
def almacen(request):
 
    producto=Producto.objects.all()    #obtenemos todos los obj de la clase Vehiculo
    datos={'esculturas' : producto}     #creamos diccionario que recibe la colección de objetos
    return render(request, 'almacen.html', datos)   #enviamos parámetro al template


@login_required
def crear(request):
    if request.method=='POST':
        esculturaform = EsculturasForm(request.POST, request.FILES)
        if esculturaform.is_valid():
            esculturaform.save()     #similar al insert en función
            return redirect('almacen')
    else:
        esculturaform=EsculturasForm()
    return render(request, 'crear.html',{'esculturaform': esculturaform})

@login_required
def eliminar(request, id):
    productoEliminado=Producto.objects.get(idproducto=id)  #obtenemos un objeto por su pk
    productoEliminado.delete()
    return redirect('almacen')

@login_required
def modificar(request,id):
    productos = Producto.objects.get(idproducto=id)         #obtenemos un objeto por su pk
    datos ={
        'form':EsculturasForm(instance=productos)
    }
    if request.method=='POST':
        formulario = EsculturasForm(data=request.POST, instance=productos)
        if formulario.is_valid:
            formulario.save()
            return redirect ('almacen')
    return render(request, 'modificar.html', datos)

def registrar(request):
    data={
        'form' : RegistroUserForm()
    }
    if request.method == 'POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('principal')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

@login_required
def mostrar(request):
    esculturas =Producto.objects.all()
    datos={
        'esculturas' : esculturas
    }
    return render(request,'mostrar.html',datos)