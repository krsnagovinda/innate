from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView

from .forms import ClinicaForm
from .models import Clinica, Welcome_Area


# vistas de pagina web
def home(request):
    return render(request, 'home.html')

def acerca(request):
    return render(request, 'acerca.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def precios(request):
    return render(request, 'precios.html')

def get_first_element(request):
    objetos = Clinica.objects.all()   
    calendario = objetos[:1]
    context = {'calendario':calendario}    
    return render(request, 'calendario/google_calendar.html', context)


#   vistas CRUD de clinica


