from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone

from .forms import ConsultaForm
from .models import  Consulta
from paciente.models import Paciente
from persona.models import Persona

# Create your views here.

def index(request):
    consultas = Consulta.objects.order_by('-id')
    

    paginator = Paginator(consultas,10)
    contador = Consulta.objects.all().count()

    page = request.GET.get('page')
    paged_consultas = paginator.get_page(page)

    context = {'consultas' : paged_consultas, 'contador':contador}
    return render (request, 'consulta_lista.html', context)

def detalle(request,pk):
    paciente = Paciente.objects.get(id=pk)    
    detalle_cons = paciente.consulta_set.all()    
    context = {'detalle_cons': detalle_cons}
    
    return render(request, 'consultas_paciente.html', context)


def detalle_doctor(request, pk):
    doctor = Persona.objects.get(id=pk)
    detalle_pertenece = doctor.Consulta_set.all()

    context = {
        'detalle_pettenece':detalle_pertenece
    }
    
    return render(request, 'consultas_medico.html', context)



class UploadConsultaView(SuccessMessageMixin, CreateView):
    model = Consulta
    login_required = True
    form_class = ConsultaForm    
    template_name = 'upload_consulta.html'
    success_messagge = "Consulta creada correctamente"
    
    def get_success_url(self):
        return reverse('class_consulta_detail', kwargs={'pk': self.object.id})

    
class ConsultaDetailView(DetailView):
    model = Consulta
    login_required = True
    template_name = 'consulta_detail.html'
    queryset = Consulta.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Consulta, id=id_)

class ConsultaUpdateView(SuccessMessageMixin, UpdateView):
    model = Consulta
    login_required = True
    template_name = 'consulta_form.html'
    fields = [            
              'transoral_neutra',
              'transoral_dinamica_derecha',
              'transoral_dinamica_izquierda',
              'AP_cervical',
              'AP_toraxica',
              'AP_lumbopelvica',
              'lateral_cervical',
              'lateral_toraxica',
              'lateral_lumbopelvica',
              'cervical_extension',
              'cervical_flexion',
              'stitch_AP',
              'stitch_lateral',
              'posturometria_frente',
              'posturometria_lateral',
              'posturometria_posterior',
              'scanner',
              'extra_1',
              'extra_2',
              'foto',
            ]
    success_messagge = "Imágenes añadidas correctamente"
    
    def get_success_url(self):
        return reverse('class_consulta_detail', kwargs={'pk': self.object.id})

class ConsultaDeleteView(DeleteView):
    model = Consulta
    login_required = True
    template_name = 'consulta_delete.html'
    success_url = reverse_lazy('class_consulta_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Consulta, id=id_)
