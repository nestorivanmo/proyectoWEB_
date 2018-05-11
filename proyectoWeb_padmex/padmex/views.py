from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Detalle, Cliente, Producto
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'padmex/index.html'
    def get_queryset(self):
        return Detalle.objects.all()

class VerOlimpicas(generic.ListView):
    model = Detalle
    template_name = 'padmex/olimpicas.html'

class VerResidenciales(generic.ListView):
    template_name = 'padmex/residenciales.html'
    def get_queryset(self):
        return Detalle.objects.all()

class VerCompras(generic.ListView):

    template_name = 'padmex/compras.html'
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
















