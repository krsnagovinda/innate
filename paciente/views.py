from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User, Group, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.views import generic
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.db.models import Q, Count
from django.utils import timezone
from datetime import date, timedelta, datetime

from django.views.generic.detail import SingleObjectMixin
from django.forms import inlineformset_factory



from .models import Paciente, Cuaderno, Notas_Extra
from .forms import PacienteForm, CuadernoForm, Notas_ExtraForm
from consulta.models import Consulta
from consulta.forms import ConsultaForm
from clinica.models import Clinica


# Genera número Random



# Vista de contador pacientes
def index(request):
    pacientes = Paciente.objects.order_by('-id')
    paginator = Paginator(pacientes,10)
    contador = Paciente.objects.all().count()

    page = request.GET.get('page')
    paged_pacientes = paginator.get_page(page)

    context = {'pacientes' : paged_pacientes, 'contador':contador}
    return render (request, 'lista-pacientes.html', context)


# vista para renderizar el primer objeto del modelo Clinica
def get_first_element(request):
    objetos = Clinica.objects.all()
    calendario = objetos[:1]
    context = {'calendario':calendario}
    return render(request, 'calendario/google_calendar.html', context)


# Vista de Search

class SearchResultsView(ListView):
    model = Paciente
    template_name = 'paciente/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paciente.objects.filter(
            Q(record__icontains=query) | Q(Nombre__icontains=query) | Q(Apellido_Paterno__icontains=query) | Q(Apellido_Materno__icontains=query)
        )
        return object_list

def SearchResultsFechaView(request):
        if request.method=="POST":
            fromdate=request.POST.get('fromdate')
            todate=request.POST.get('todate')
            t=Paciente.objects.filter(Q(creada__gte=fromdate)&Q(creada__lte=todate))
            return render(request, 'paciente/search_results_fecha.html',{"data":t})

        else:
            displaydata=Paciente.objects.all()
            return render(request, 'paciente/search_results_fecha.html', {"data":displaydata})


#### vistas CRUD de Paciente

# vista de listas pagina detalle del paciente

def paciente_detalle(request, pk):
    paciente = Paciente.objects.get(id=pk)
    consultas = paciente.consulta_set.all()[:1]
    consultas_count = consultas.count()
    cuadernos = paciente.cuaderno_set.all()[:1]
    cuadernos_count = cuadernos.count()
    notas_extra = paciente.notas_extra_set.all()[:1]
    notas_extra_count = notas_extra.count()    
    link = "http://170.64.156.218/pacientes/paciente/"+ str(Paciente.objects.get(id=pk))


    context={'consultas':consultas, 'paciente':paciente,
             'consultas_count':consultas_count, 'cuadernos':cuadernos,
             'cuadernos_count':cuadernos_count, 'notas_extra':notas_extra,
             'notas_extra_count':notas_extra_count,
             'link': link }

    return render(request, 'paciente/paciente_detail.html', context)

# vista para crear consulta desde perfil de paciente, cuaderno y notas
def createConsulta(request, pk):
    ConsultaFormSet = inlineformset_factory(Paciente, Consulta, fields=('start_time', 'sesion', 'atiende', 'Padecimiento_actual', 'Ajuste_de_hoy', 'general',
              'cervical', 'toraxica', 'lumbo_sacra', 'sacro_iliaco', 'coccix', 'pelvis_cadera',
              'curvatura', 'cefaleas', 'hombro', 'codo_a_mano', 'rodilla', 'pronostico',
              'notas', 'end_time'), extra=1)
    paciente = Paciente.objects.get(id=pk)
    formset = ConsultaFormSet(queryset=Consulta.objects.none(), instance=paciente)
    #form = ConsultaForm(initial={'paciente':paciente})
    if request.method == 'POST':
        #form = ConsultaForm(request.POST)
        formset = ConsultaFormSet(request.POST, instance=paciente)
        if formset.is_valid():
            formset.save()
            return redirect('lista_consultas', paciente.pk)
    context = {'formset':formset}
    return render(request, 'paciente/consulta_form.html', context)


def createCuaderno(request, pk):
    CuadernoFormSet = inlineformset_factory(Paciente, Cuaderno, CuadernoForm, extra=1)
    paciente = Paciente.objects.get(id=pk)
    formset = CuadernoFormSet(queryset=Cuaderno.objects.none(), instance=paciente)
    if request.method == 'POST':
        formset = CuadernoFormSet(request.POST, instance=paciente)
        if formset.is_valid():
            formset.save()
            return redirect ('lista_cuadernos', paciente.pk)
    context = {'formset':formset}
    return render(request, 'paciente/cuaderno_form.html', context)

def createNotas_Extra(request, pk):
    Notas_ExtraFormSet = inlineformset_factory(Paciente, Notas_Extra, fields=('titulo', 'texto'), extra=1)
    paciente = Paciente.objects.get(id=pk)
    formset = Notas_ExtraFormSet(queryset=Notas_Extra.objects.none(), instance=paciente)
    if request.method == 'POST':
        formset = Notas_ExtraFormSet(request.POST, instance=paciente)
        if formset.is_valid():
            formset.save()
            return redirect ('lista_notas_extra', paciente.pk)
    context = {'formset':formset}
    return render(request, 'paciente/Notas_Extra_form.html', context)


# CRUD paciente
class UploadPacienteView(SuccessMessageMixin, CreateView):
    model = Paciente
    login_required = True
    form_class = PacienteForm
    success_url = reverse_lazy('pacientes_lista')
    template_name = 'paciente/upload_paciente.html'
    success_message = "Paciente registrado correctamente "


class PacienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Paciente
    login_required = True
    template_name = 'paciente/paciente_form.html'
    fields = ['record',
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
    success_message = "Datos de Paciente editados correctamente"
    def get_success_url(self):
        return reverse('detalle_paciente', kwargs={'pk': self.object.id})


class PacienteDeleteView(SuccessMessageMixin, DeleteView):
    model = Paciente
    login_required = True
    template_name = 'paciente/paciente_delete.html'
    success_url = reverse_lazy('pacientes_lista')
    

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Paciente, id=id_)

def prueba(request,id):
    model = Paciente
    template_name = 'paciente/prueba.html'
    queryset = Paciente.objects.all()
    current_day = date.today().day
    current_month = date.today().month
    current_year = date.today().year

    def get_objects(self):
        pk_ = self.kwargs.get("id")
        return get_object_or_404(Paciente, pk=id_)

    context = {'current_day':current_day, 'current_month':current_month, 'current_year':current_year}
    return render(request, 'prueba.html', context)


# CRUD cuaderno

def lista_cuadernos(request, pk):
    paciente = Paciente.objects.get(id=pk)
    cuadernos = paciente.cuaderno_set.all()
    context = {'cuadernos':cuadernos}

    return render(request, 'cuaderno/cuadernos_paciente.html', context)

class CuadernoUpdateView(UpdateView):
    model = Cuaderno
    login_required = True
    template_name = 'cuaderno/cuaderno_form.html'
    fields = [
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
    success_messagge = "Imágenes añadidas correctamente"

    def get_success_url(self):
        return reverse('class_cuaderno_detail', kwargs={'pk': self.object.id})


class CuadernoDetailView(DetailView):
    model = Cuaderno
    login_required = True
    template_name = 'cuaderno/cuaderno_detail.html'
    queryset = Cuaderno.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cuaderno, id=id_)


class CuadernoDeleteView(DeleteView):
    model = Cuaderno
    login_required = True
    template_name = 'cuaderno/cuaderno_delete.html'
    success_url = reverse_lazy('lista_cuadernos')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cuaderno, id=id_)


# CRUD notas extra
def lista_notas_extra(request, pk):
    paciente = Paciente.objects.get(id=pk)
    notas_extra = paciente.notas_extra_set.all()
    context = {'notas_extra':notas_extra}

    return render(request, 'notasExtra/notasExtra_paciente.html', context)

class Notas_ExtraDetailView(DetailView):
    model = Notas_Extra
    login_required = True
    template_name = 'notasExtra/notas_extra_detail.html'
    queryset = Notas_Extra.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Notas_Extra, id=id_)

class Notas_EXtraDeleteView(DeleteView):
    model = Notas_Extra
    login_required = True
    template_name = 'notasExtra/notas_extra_delete.html'
    success_url = reverse_lazy('pacientes_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Notas_Extra, id=id_)

class Notas_EXtraUpdateView(UpdateView):
    model = Notas_Extra
    login_required = True
    template_name = 'notasExtra/notas_extra_form.html'
    fields = [
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
    def get_success_url(self):
        return reverse('class_notas_extra_detail', kwargs={'pk': self.object.id})


class logOut(generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, "user logged out")
        return redirect('panel2')