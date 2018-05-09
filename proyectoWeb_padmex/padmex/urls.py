from django.urls import path, re_path
from . import views

urlpatterns = [
    # /padmex/
    path('', views.IndexView.as_view(), name='index'),
    path('olimpicas', views.DetailView.as_view(), name="olimpicas")

    # /padmex/olimpicas
    #path('olimpicas', views.olimpicas, name='olimpicas'),

    # /padmex/cliente_id
   # re_path(r'olimpicas/(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='olimpicas'),
]
