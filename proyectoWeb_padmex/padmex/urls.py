from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'padmex'

urlpatterns = [
    # /padmex/

    path('olimpicas', views.VerOlimpicas.as_view(), name="olimpicas"),
    path('residenciales', views.VerResidenciales.as_view(), name="residenciales"),
    path('nosotros', views.VerNosotros.as_view(), name="nosotros"),
    path('productos', views.VerProductos.as_view(), name="productos"),
    re_path(r'^productos/(?P<pk>[0-9]+)/$', views.DetailViews.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('comprar', views.VerCompras, name="compras"),
    path('entrar', views.VerControladorLogin.as_view(), name="controlador"),
    path('carrito', views.VerCarrito.as_view(), name="carrito"),
    path('ubicaciones', views.VerUbicaciones.as_view(), name="ubicaciones"),
    path('contactanos', views.VerContacto.as_view(), name="contactanos"),
    path('galeria', views.VerGaleria.as_view(), name="galeria"),
    path('citas', views.AgendarCita, name="citas"),
    #path(r'productos/add/$', views.UserCreate.as_view(), name='cliente-add'),
]
