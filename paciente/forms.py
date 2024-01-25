from django.forms import (
    ModelForm, Textarea, EmailInput, DateInput, TextInput, inlineformset_factory
    )
from . models import Paciente, Cuaderno, Notas_Extra
from django import forms
from decimal import Decimal, DecimalException
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields =[
            'record',
            'Titulo',
            'Apellido_Paterno',
            'Apellido_Materno',
            'Nombre',
            'Fecha_Nacimiento',
            'Sexo',
            'Domicilio',
            'Ciudad',
            'Telefono',
            'Email',
            'photo_1',
            ]

        widgets ={
                  'Email': EmailInput(),
                  'Fecha_Nacimiento': DateInput(),
                  }

        labels = {
            'record' : 'Número de Ficha Clínica ',
            'photo_1': 'Foto del Perfil',
                }
        help_texts = {
            'Fecha_Nacimiento': 'dd/mm/aaaa',
        }



class CuadernoForm(ModelForm):
    class Meta:
        model = Cuaderno
        fields =[
            'record',
            'titulo',
            'texto',
            'estatura',
            'peso',
            'presion',
            'temperatura',
            'toxicologico',
            'interrogatorio',
            'exploracion',
            'estudios',
            ]
        labels = {
            'presion' : 'Presión Sanguinea MM/Hg',
            'estatura': 'Estatura en cm.',
            'peso': 'Peso en Kg.',
            'temperatura': 'Temperatura en ºC',

                }

class Notas_ExtraForm(ModelForm):
    class Meta:
        model = Notas_Extra
        fields =[
            'refiere',
            'titulo',
            'texto',
            'imagen_1',
            'imagen_2',
            'imagen_3',
            'imagen_4',
            'imagen_5',
            'imagen_6',
            'imagen_7',
            'imagen_8',
            'imagen_9',
            'imagen_10',
            ]
