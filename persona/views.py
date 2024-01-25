from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q, Count

from django.urls import reverse_lazy ,reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.forms import inlineformset_factory

from paciente.models import Paciente
from consulta.models import Consulta
from clinica.models import Clinica
from consulta.forms import ConsultaForm
from .forms import PersonaForm
from .models import Persona


# funcion para mostrar pagina home
def home(request):
    return render(request, 'home.html')

# funcion para mostrar pagina panel, solo 5 elementos
def panel2(request):
    monos = Paciente.objects.all()[:5]
    chambiador = Persona.objects.all()[:5]
    terapias = Consulta.objects.all()[:5]
    objetos = Clinica.objects.all
    context = {'monos':monos, 'chambiador':chambiador, 'terapias':terapias, 'objetos':objetos}

    return render(request, 'back/panel2.html', context)



def index(request):
    personas = Persona.objects.order_by('-id')
    contador = Persona.objects.all().count()
    paginator = Paginator(personas,10)
    page = request.GET.get('page')
    paged_pẹrsonas = paginator.get_page(page)

    quiro = Persona.objects.filter(Rol='Quiropráctico').count()
    asistant = Persona.objects.filter(Rol='Asistente').count()
    radio = Persona.objects.filter(Rol='Radiólogo').count()
    cap = Persona.objects.filter(Rol='Capacitación').count()
    conta = Persona.objects.filter(Rol='Contabilidad').count()
    admins = Persona.objects.filter(Rol='Administrador').count()



    context = {'personas':paged_pẹrsonas, 'contador':contador, 'quiro':quiro, 'asistant':asistant, 'radio':radio, 'cap':cap, 'conta':conta, 'admins':admins}
    return render(request, 'usuarios_lista.html', context)


# Vista de Search

class SearchResultsView(ListView):
    model = Persona
    template_name = 'search_results_user.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Persona.objects.filter(
            Q(id__icontains=query) | Q(Nombre__icontains=query) | Q(Apellido_Paterno__icontains=query) | Q(Apellido_Materno__icontains=query) | Q(Rol__icontains=query) | Q(email__icontains=query)
        )
        return object_list


#VISTAS PARA LISTAR ELEMENTOS
def quiro3(request):
    quiro_lista = Persona.objects.filter(Rol='Quiropráctico')
    personas = Persona.objects.all().count()
    quiro = Persona.objects.filter(Rol='Quiropráctico').count()
    asistant = Persona.objects.filter(Rol='Asistente').count()
    radio = Persona.objects.filter(Rol='Radiólogo').count()
    cap = Persona.objects.filter(Rol='Capacitación').count()
    conta = Persona.objects.filter(Rol='Contabilidad').count()
    admins = Persona.objects.filter(Rol='Administrador').count()

    context = {'quiro_lista':quiro_lista, 'personas':personas, 'quiro':quiro, 'asistant':asistant, 'radio':radio, 'cap':cap, 'conta':conta, 'admins':admins}
    return render(request, 'quiro_lista.html', context)


def asistente(request):
    asistant_lista = Persona.objects.filter(Rol='Asistente')
    personas = Persona.objects.all().count()
    asistant = Persona.objects.filter(Rol='Asistente').count()
    quiro = Persona.objects.filter(Rol='Quiropráctico').count()
    radio = Persona.objects.filter(Rol='Radiólogo').count()
    cap = Persona.objects.filter(Rol='Capacitación').count()
    conta = Persona.objects.filter(Rol='Contabilidad').count()
    admins = Persona.objects.filter(Rol='Administrador').count()

    context = {'asistant_lista':asistant_lista, 'personas':personas, 'quiro':quiro, 'asistant':asistant, 'radio':radio, 'cap':cap, 'conta':conta, 'admins':admins}
    return render(request, 'asistente_lista.html', context)


def radiologo(request):
    radio_lista = Persona.objects.filter(Rol='Radiólogo')
    personas = Persona.objects.all().count()
    radio = Persona.objects.filter(Rol='Radiólogo').count()
    asistant = Persona.objects.filter(Rol='Asistente').count()
    quiro = Persona.objects.filter(Rol='Quiropráctico').count()
    cap = Persona.objects.filter(Rol='Capacitación').count()
    conta = Persona.objects.filter(Rol='Contabilidad').count()
    admins = Persona.objects.filter(Rol='Administrador').count()

    context = {'radio_lista':radio_lista, 'personas':personas, 'radio':radio, 'quiro':quiro, 'asistant':asistant, 'cap':cap, 'conta':conta, 'admins':admins}
    return render(request, 'radiologo_lista.html', context)

def capa(request):
    capa_lista = Persona.objects.filter(Rol='Capacitación')
    personas = Persona.objects.all().count()
    radio = Persona.objects.filter(Rol='Radiólogo').count()
    asistant = Persona.objects.filter(Rol='Asistente').count()
    quiro = Persona.objects.filter(Rol='Quiropráctico').count()
    cap = Persona.objects.filter(Rol='Capacitación').count()
    conta = Persona.objects.filter(Rol='Contabilidad').count()
    admins = Persona.objects.filter(Rol='Administrador').count()

    context = {'capa_lista':capa_lista, 'personas':personas, 'radio':radio, 'quiro':quiro, 'asistant':asistant, 'cap':cap, 'conta':conta,  'admins':admins}
    return render(request, 'capa_lista.html', context)

def contable(request):
    conta_lista = Persona.objects.filter(Rol='Contabilidad')
    personas = Persona.objects.all().count()
    radio = Persona.objects.filter(Rol='Radiólogo').count()
    asistant = Persona.objects.filter(Rol='Asistente').count()
    quiro = Persona.objects.filter(Rol='Quiropráctico').count()
    cap = Persona.objects.filter(Rol='Capacitación').count()
    conta = Persona.objects.filter(Rol='Contabilidad').count()
    admins = Persona.objects.filter(Rol='Administrador').count()

    context = {'conta_lista':conta_lista, 'personas':personas, 'radio':radio, 'quiro':quiro, 'asistant':asistant, 'cap':cap, 'conta':conta,  'admins':admins}
    return render(request, 'conta_lista.html', context)


def admins(request):
    admins_lista = Persona.objects.filter(Rol='Administrador')
    personas = Persona.objects.all().count()
    radio = Persona.objects.filter(Rol='Radiólogo').count()
    asistant = Persona.objects.filter(Rol='Asistente').count()
    quiro = Persona.objects.filter(Rol='Quiropráctico').count()
    cap = Persona.objects.filter(Rol='Capacitación').count()
    conta = Persona.objects.filter(Rol='Contabilidad').count()
    admins = Persona.objects.filter(Rol='Administrador').count()

    context = {'admins_lista':admins_lista, 'personas':personas, 'radio':radio, 'quiro':quiro, 'asistant':asistant, 'cap':cap, 'conta':conta, 'admins':admins}
    return render(request, 'admins_lista.html', context)



# vistas CRUD de Personas
class UploadPersonaView(CreateView):
    model = Persona
    login_required = True
    form_class = PersonaForm
    success_url = reverse_lazy('class_personas_lista')
    template_name = 'upload_usuario.html'

class PersonaDetailView(DetailView):
    model = Persona
    login_required = True
    template_name = 'usuario_detail.html'
    queryset = Persona.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Persona, id=id_)

class PersonaUpdateView(UpdateView):
    model = Persona
    login_required = True
    template_name = 'usuario_form.html'
    fields = [
              'user',
              'Nombre',
              'Apellido_Paterno',
              'Apellido_Materno',
              'Rol',
              'Cedula',
              'Telefono',
              'email',
              'Foto',
              'facebook',
              'twitter',
              'linkedin',
              'instagram',

              ]
    success_url = reverse_lazy('class_personas_lista')

class PersonaDeleteView(DeleteView):
    model = Persona
    login_required = True
    template_name = 'usuario_delete.html'
    success_url = reverse_lazy('class_personas_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Persona, id=id_)


  
