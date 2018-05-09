from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Cliente

def index(request):
    all_clients = Cliente.objects.all()
    template = loader.get_template('padmex/index.html')
    context = {'all_clients':all_clients,}
    return HttpResponse(template.render(context,request))

def albercaOlimpica(request, cliente_id):
    return HttpResponse("<h3>alebrcas olimpicas" + str(cliente_id) + "</h3>")
