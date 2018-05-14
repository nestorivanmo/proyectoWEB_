from django import forms
from . import models

class AgendarCita(forms.ModelForm):
    class Meta:
        model = models.Cita
        fields = ['asunto','contenido','telefono', 'correo']