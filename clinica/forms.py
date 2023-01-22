from django.forms import ModelForm, Textarea, EmailInput, DateInput
from . models import Clinica
from django import forms
from decimal import Decimal, DecimalException


class ClinicaForm(ModelForm):
    class Meta:
        model = Clinica
        fields = ['Nombre_Clinica', 'Direccion', 'Telefono', 'icono', 'url']
        widgets ={
                 }

        labels = {

            'Nombre_Clinica' : 'Nombre de la Clínica',
                }
        required = True,
