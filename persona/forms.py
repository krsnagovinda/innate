from django.forms import ModelForm, Textarea, EmailInput, DateInput
from . models import Persona
from django import forms
from decimal import Decimal, DecimalException

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['user', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Rol', 'Cedula', 'Telefono', 'email', 'Foto', 'facebook', 'twitter', 'linkedin', 'instagram']
        widgets ={
                 }

        labels = {

            'Nombre' : 'Nombre del Usuario',
                }
        required = True,
