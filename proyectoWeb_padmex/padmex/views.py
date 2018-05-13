from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Detalle, Cliente, Producto
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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

class VerCarrito(generic.ListView):
    template_name = 'padmex/carrito.html'
    def get_queryset(self):
        return Detalle.objects.all()

class VerNosotros(generic.ListView):
    template_name = 'padmex/nosotros.html'
    def get_queryset(self):
        return Detalle.objects.all()

class VerProductos(generic.ListView):
    template_name = 'padmex/productos.html'
    def get_queryset(self):
        return Detalle.objects.all()

class DetailViews(generic.DetailView):
    model = Producto
    template_name = 'padmex/producto_form.html'

class VerControladorLogin(generic.ListView):
    template_name = 'padmex/controladorLogin.html'
    def get_queryset(self):
        return Detalle.objects.all()
















