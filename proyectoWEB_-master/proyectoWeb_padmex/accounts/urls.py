from django.conf.urls import url
from . import views

# Create your views here -> VA!

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^recuperar/$', views.recuperar_view, name="recuperar"),

]
