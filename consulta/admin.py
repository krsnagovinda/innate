from django.contrib import admin
from .models import Consulta

# Register your models here.

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pertenece', 'creada', 'modificada', 'start_time', 'end_time', 'atiende']
    list_filter = ['id', 'pertenece', 'start_time', 'end_time', 'atiende']
    search_fields = ['id', 'pertenece', 'creada', 'modificada', 'start_time', 'end_time', 'atiende']
    list_per_page = 25


admin.site.register(Consulta, ConsultaAdmin)
