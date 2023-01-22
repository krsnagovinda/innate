from django.db import models
from imagekit.models import ProcessedImageField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from datetime import date, timedelta, datetime

from persona.models import Persona

# Create your models here.
class Paciente(models.Model):
    sexo_opciones= (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    titulo_opciones= (
        ('Sr', 'Señor'),
        ('Sra', 'Señora'),
        ('Srita', 'Señorita'),
        ('Joven', 'Joven'),
    )
    record = models.CharField(max_length=50, null=True, unique=True)
    Titulo = models.CharField(max_length=50, choices=titulo_opciones, null=True, blank=True, default="Sr.")
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=50)
    Fecha_Nacimiento = models.DateField()
    Sexo = models.CharField(max_length=1, choices=sexo_opciones, default="M")
    Domicilio = RichTextUploadingField(blank=True, null=True)
    Ciudad = models.CharField(max_length=30, blank=True, null=True, default="CDMX")
    Telefono = models.CharField(max_length=30, blank=True, null=True )
    Email = models.EmailField(null=True, blank=True)
    photo_1 = models.ImageField(default='default.jpg', upload_to='pacientes/fotos/%Y/%m/%d/', blank=True, null=True)
    creada = models.DateTimeField(auto_now_add=True)
    modificada = models.DateTimeField(auto_now=True)

    class Meta:
      verbose_name_plural = "pacientes"
      ordering = ("-id",)

    def otro_nombre(self):
        return self.Nombre + '  ' + self.Apellido_Paterno + '  ' + self.Apellido_Materno
    
    def get_fullname(self):
        return self.record 

    def __str__(self):
        return self.get_fullname()


    @property
    def calculo_edad(self):
        today = date.today()
        año_actual = today.year
        mes_actual = today.month
        dia_actual = today.day
        paciente_año = self.Fecha_Nacimiento.year
        paciente_mes = self.Fecha_Nacimiento.month
        paciente_dia = self.Fecha_Nacimiento.day

        edad_paciente = año_actual - paciente_año - ((mes_actual, dia_actual) < (paciente_mes, paciente_dia))

        return edad_paciente

class Cuaderno(models.Model):
    record = models.ForeignKey(Paciente, on_delete=models.CASCADE, help_text="seleccione el paciente que corresponde")
    titulo = models.CharField(max_length=100)
    texto = RichTextUploadingField(blank=True, null=True)
    estatura = models.CharField(max_length=500, blank=True, null=True)
    peso = models.CharField(max_length=500, blank=True, null=True)
    presion = models.CharField(max_length=500, blank=True, null=True)
    temperatura = models.CharField(max_length=500, blank=True, null=True)
    toxicologico = models.CharField(max_length=500, blank=True, null=True)
    interrogatorio = models.CharField(max_length=500, blank=True, null=True)
    exploracion = models.CharField(max_length=500, blank=True, null=True)
    estudios = models.CharField(max_length=500, blank=True, null=True)
    imagen_1 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_2 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_3 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_4 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_5 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_6 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_7 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_8 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_9 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    imagen_10 = ProcessedImageField(upload_to='paciente_notas_evolucion', blank=True, null=True)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Cuadernos'
        ordering = ("-id",)
        get_latest_by = ['creada']

    def __str__(self):
        return str(self.titulo)

class Notas_Extra(models.Model):
    refiere = models.ForeignKey(Paciente, on_delete=models.CASCADE, help_text="seleccione el paciente que corresponde")
    titulo = models.CharField(max_length=100)
    texto = RichTextUploadingField(blank=True, null=True)
    imagen_1 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_2 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_3 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_4 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_5 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_6 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_7 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_8 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_9 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    imagen_10 = models.ImageField(upload_to='paciente_notas_extra', blank=True, null=True)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Notas_Extra'
        ordering = ("-id",)
        get_latest_by = ['creada']

    def __str__(self):
        return str(self.titulo)
