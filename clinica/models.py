from django.db import models
from django import forms
from imagekit.models import ProcessedImageField

class Clinica(models.Model):
    Nombre_Clinica = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=20)
    icono = ProcessedImageField(upload_to='clinica_media/', blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.Nombre_Clinica


class Welcome_Area(models.Model):
    slogan_1 = models.CharField(max_length=100)
    slogan_2 = models.CharField(max_length=100)
    slogan_3 = models.CharField(max_length=100)
    slogan_4 = models.CharField(max_length=100)
    imagen_1 = ProcessedImageField(upload_to='clinica_website/welcome_area/', blank=True, null=True)
    imagen_2 = ProcessedImageField(upload_to='clinica_website/welcome_area/', blank=True, null=True)

    def __str__(self):
        return self.id

