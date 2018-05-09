from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente

def index(request):
    all_clients = Cliente.objects.all()
    context = {'all_clients':all_clients,}
    return render(request, 'padmex/index.html', context)

def olimpicas(request):
    all_clients = Cliente.objects.all()
    return render(request, 'padmex/olimpicas.html', {'all_clients': all_clients, })

def detail(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise Http404("No se encuentra la página -> padmex")
    return render(request, 'padmex/details.html', {'cliente':cliente,})


def albercaOlimpica(request, cliente_id):
    return HttpResponse("<h3>alebrcas olimpicas" + str(cliente_id) + "</h3>")
