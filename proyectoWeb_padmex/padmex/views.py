from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Detalle, Cliente, Producto
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm




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

class VerProductos(generic.ListView):
    template_name = 'padmex/productos.html'
    def get_queryset(self):
        return Detalle.objects.all()

class DetailViews(generic.DetailView):
    model = Producto
    template_name = 'padmex/producto_form.html'

class UserCreate(CreateView):
    model = Cliente
    fields = ['nombre', 'usuario', 'passwd', 'correo', 'telefono']

class UserFormView(View):
    form_class = UserForm
    template_name = 'padmex/registrationForm.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #request.user.username
                    return redirect('padmex:index')

        return render(request, self.template_name, {'form': form})














