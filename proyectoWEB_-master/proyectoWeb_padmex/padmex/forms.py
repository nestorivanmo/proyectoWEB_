from django import forms
from django.forms import SelectDateWidget
from . import models


class AgendarCita(forms.ModelForm):
    #  fechaCita = forms.DateField(widget=SelectDateWidget(empty_label=("Choose year")))
    class Meta:
        model = models.Cita
        fields = ['asunto','contenido','teléfono', 'correo',]

