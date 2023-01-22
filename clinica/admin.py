from django.contrib import admin
from .models import Clinica, Welcome_Area

# Register your models here.
class ClinicaAdmin(admin.ModelAdmin):
    fields= ['Nombre_Clinica', 'Direccion', 'Telefono', 'icono','url']
    list_display = ['id','Nombre_Clinica', 'Direccion', 'Telefono']
    list_filter = []
    search_fields = ['id', 'Nombre_Clinica', 'Direccion','Telefono']

class Welcome_AreaAdmin(admin.ModelAdmin):
    fields= ['slogan_1', 'slogan_2', 'slogan_3', 'slogan_4', 'imagen_1', 'imagen_2']
    list_display = ['id']
    list_filter = []
    

admin.site.register(Clinica)
admin.site.register(Welcome_Area)
