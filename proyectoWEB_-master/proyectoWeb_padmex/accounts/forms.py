from django import forms
from django.forms import SelectDateWidget
from padmex import models


class EnviarCorreo(forms.ModelForm):
    class Meta:
        model = models.Cita
        fields = ['correo']

