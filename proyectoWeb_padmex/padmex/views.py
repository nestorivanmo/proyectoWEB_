from django.views import generic
from django.views.generic import View
from .models import Detalle
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'padmex/index.html'

    def get_queryset(self):
        return Detalle.objects.all()

class DetailView(generic.ListView):
    model = Detalle
    template_name = 'padmex/olimpicas.html'

class UserFormView(View):
    form_class = UserForm