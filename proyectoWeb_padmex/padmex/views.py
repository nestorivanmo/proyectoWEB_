from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Detalle, Cliente, Producto
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

carrito = [[-1,-1]]


class IndexView(generic.ListView):
    template_name = 'padmex/index.html'
    def get_queryset(self):
        return Detalle.objects.all()

class VerOlimpicas(generic.ListView):
    model = Detalle
    template_name = 'padmex/olimpicas.html'

class VerUbicaciones(generic.ListView):
    model = Detalle
    template_name = 'padmex/ubicaciones.html'

class VerContacto(generic.ListView):
    model = Detalle
    template_name = 'padmex/contactanos.html'

class VerGaleria(generic.ListView):
    model = Detalle
    template_name = 'padmex/galeria.html'

class VerResidenciales(generic.ListView):
    template_name = 'padmex/residenciales.html'
    def get_queryset(self):
        return Detalle.objects.all()

@login_required(login_url="/accounts/login")
def VerCompras(request):
    return render(request, 'padmex/compras.html')

def Exito(request):
    return render(request, 'padmex/exito.html')

@login_required(login_url="/accounts/login")
def AgendarCita(request):
    if request.method == 'POST':
        form = forms.AgendarCita(request.POST)
        if form.is_valid():
            # guardar datos en la BD
            instance = form.save(commit=False)
            instance.cliente_FK = request.user
            instance.save()
            return redirect('padmex:exito')  # que nos mande a un html donde veamos nuestras citas
    else:
        form = forms.AgendarCita()
    return render(request, 'padmex/citas.html', {'form': form})

def VerCarrito(request, pk_cliente):
    tam = len(carrito)
    i = 0
    encontro = 0
    while i < tam:
        if carrito[i][0] == pk_cliente:
            encontro = 1
            return render(request, 'padmex/carrito.html', {'productos': carrito[i]})
            break
        i += 1

    if encontro == 0:
        return render(request, 'padmex/galeria.html')



class VerNosotros(generic.ListView):
    template_name = 'padmex/nosotros.html'
    def get_queryset(self):
        return Detalle.objects.all()

class VerProductos(generic.ListView):
    template_name = 'padmex/productos.html'
    def get_queryset(self):
        return Producto.objects.all()

@login_required(login_url='/accounts/login')
def DetailViews(request, pk_cliente, pk):
    # model = Producto
    # Agregar al carrito -> productos
    # template_name = 'padmex/carrito.html'
    tam = len(carrito)
    i = 0
    encontro = 0
    lista = []
    if carrito[0][0] == -1:
            carrito[0][0] = pk_cliente
            carrito[0][1] = pk
            encontro = 1

    else:
            while i < tam:
                if carrito[i][0] == pk_cliente:
                    encontro = 1
                    carrito[i].append(pk)
                i += 1

    if encontro == 0:
        carrito.append([pk_cliente, pk])

    j = 1
    tamCarr = 0
    posU = 0
    prods = []

    while i < tam:
        if carrito[i][0] == pk_cliente:
            tamCarr = len(carrito[i])
            posU = i
            break
        i += 1

    while j < tamCarr:
        nombre = Producto.objects.filter(id=carrito[posU][j]).values('nombreProd', 'descripcionProd', 'precio')
        prods.append(nombre)
        j += 1

    return render(request, 'padmex/carrito.html', {'productos': prods})


class VerControladorLogin(generic.ListView):
    template_name = 'padmex/controladorLogin.html'
    def get_queryset(self):
        return Detalle.objects.all()




















