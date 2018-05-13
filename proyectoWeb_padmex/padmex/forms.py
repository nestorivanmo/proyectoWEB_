from django import forms
from . import models

class AgendarCita(forms.ModelForm):
    class Meta:
        model = models.Cita
        fields = ['contenido','fecha']