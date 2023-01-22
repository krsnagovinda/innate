from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    rol_opciones = (
            ('Quiropráctico', 'Quiropráctico'),
            ('Asistente', 'Asistente'),
            ('Radiólogo', 'Radiólogo'),
            ('Capacitación', 'Capacitación'),
            ('Contabilidad', 'Contabilidad'),
            ('Administrador', 'Administrador')
        )
    user   = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Nombre = models.CharField(max_length=50)
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    Rol = models.CharField(max_length=15, choices=rol_opciones, default="Quiropràctico")
    Cedula = models.CharField(max_length=50, null=True, blank=True)
    Telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    Foto = models.ImageField(default='default.jpg', blank=True, upload_to='medicos/')
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)

    def get_fullname(self):
        return self.Nombre + '  ' + self.Apellido_Paterno + '  ' + self.Apellido_Materno

    class Meta:
        verbose_name = ("Personas")
        verbose_name_plural = ("Persona")
        ordering = ("-id",)

    def __str__(self):
        return self.get_fullname()
