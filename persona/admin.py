from django.contrib import admin
from .models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    fields= ['user','Nombre', 'Apellido_Paterno', 'Apellido_Materno','Rol', 'Cedula', 'Telefono', 'email', 'Foto', 'facebook', 'twitter', 'linkedin', 'instagram' ]
    list_display = ['user', 'id', 'Rol', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']
    list_filter = []
    search_fields = ['id', 'Rol', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']

admin.site.register(Persona, PersonaAdmin)