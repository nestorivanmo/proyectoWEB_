from django.urls import path, re_path
from . import views

urlpatterns = [
    # /padmex/
    path('', views.IndexView.as_view(), name='index'),
    path('olimpicas', views.VerOlimpicas.as_view(), name="olimpicas"),
    path('residenciales', views.VerResidenciales.as_view(), name="residenciales"),
    path('productos', views.VerProductos.as_view(), name="productos"),
]
