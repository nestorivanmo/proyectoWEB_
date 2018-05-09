from django.urls import path, re_path
from . import views

urlpatterns = [
    # /padmex/
    path('', views.index, name='index'),

    # /padmex/cliente_id
    re_path(r'^(?P<cliente_id>[0-9]+)/$', views.albercaOlimpica, name='albercaolimpica'),
]
