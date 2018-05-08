from django.http import HttpResponse
from .models import Cliente

def index(request):
    #all_clients = Cliente.objects.all()
    #html = ''
    #for cliente in all_clients:
     #   url = 'padmex/'+ str(cliente.id) +'/'
      #  html += '<a href='+ url +'>'+ cliente.usuario +'</a><br>'
    return HttpResponse("<h1>prueba index padmex</h1>")

def albercaOlimpica(request, cliente_id):
    return HttpResponse("<h3>alebrcas olimpicas" + str(cliente_id) + "</h3>")
