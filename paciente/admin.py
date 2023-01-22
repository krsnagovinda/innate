from django.contrib import admin
from .models import Paciente, Cuaderno, Notas_Extra
from django.contrib.auth.models import Permission

class PacienteAdmin(admin.ModelAdmin):
    fields =['record', 'Titulo', 'Apellido_Paterno', 'Apellido_Materno', 'Nombre', 'Fecha_Nacimiento',
             'Sexo', 'Domicilio', 'Ciudad', 'Telefono', 'Email', 'photo_1']
    list_display =['record', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'creada', 'modificada']
    list_filter =['record', 'creada', 'modificada']
    search_fields =['record', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'creada', 'modificada']

class CuadernoAdmin(admin.ModelAdmin):
    fields = ['record', 'titulo', 'texto', 'estatura', 'peso', 'presion', 'temperatura', 'toxicologico',
              'interrogatorio', 'exploracion', 'estudios', 'imagen_1', 'imagen_2',
             'imagen_3','imagen_4', 'imagen_5', 'imagen_6', 'imagen_7', 'imagen_8', 'imagen_9', 'imagen_10']
    list_display = ['record', 'titulo', 'creada']
    list_filter = ['record', 'titulo', 'creada']

class Notas_ExtraAdmin(admin.ModelAdmin):
    fields = ['refiere', 'titulo', 'texto', 'imagen_1', 'imagen_2',
             'imagen_3','imagen_4', 'imagen_5', 'imagen_6', 'imagen_7', 'imagen_8', 'imagen_9', 'imagen_10']
    list_display = ['refiere', 'titulo', 'creada']
    list_filter = ['refiere', 'titulo', 'creada']

admin.site.register(Cuaderno, CuadernoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Notas_Extra, Notas_ExtraAdmin)
admin.site.register(Permission)
