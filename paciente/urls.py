from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from django.conf.urls. static import static
from django.contrib.auth import views as auth_views
from paciente import views

from .views import SearchResultsView, index, SearchResultsFechaView

urlpatterns = [
    path('lista/', login_required(views.index), name='pacientes_lista'),
    path('upload_paciente/', login_required(views.UploadPacienteView.as_view()), name='class_upload_paciente'),

    path('paciente/<str:pk>/', login_required(views.paciente_detalle), name='detalle_paciente'),

    path('create_consulta/<str:pk>/', login_required(views.createConsulta), name='create_consulta'),
    path('create_NotaEvo/<str:pk>/', login_required(views.createCuaderno), name='create_cuaderno'),
    path('create_NotaExtra/<str:pk>/', login_required(views.createNotas_Extra), name='create_notasExtra'),

    path('paciente_delete/<str:pk>/', login_required(views.PacienteDeleteView.as_view()), name='class_delete_paciente'),
    path('paciente_update/<str:pk>/', login_required(views.PacienteUpdateView.as_view()), name='class_update_paciente'),

    path('buscar/', views.SearchResultsView.as_view(), name='search_results'),
    path('buscar_por_fecha/', login_required(views.SearchResultsFechaView), name='SearchResultsFecha'),

    path('delete_notaEvo/<str:pk>/', login_required(views.CuadernoDeleteView.as_view()), name='class_delete_cuaderno'),
    path('detalle_notaEvo/<str:pk>/', login_required(views.CuadernoDetailView.as_view()), name='class_cuaderno_detail'),
    path('lista_notasEvo/paciente/<str:pk>', login_required(views.lista_cuadernos), name="lista_cuadernos"),
    path('notasEvo/<str:pk>/', login_required(views.CuadernoUpdateView.as_view()), name='class_update_cuaderno'),

    path('delete_notaExtra/<str:pk>/', login_required(views.Notas_EXtraDeleteView.as_view()), name='class_delete_notas_extra'),
    path('detalle_notaExtra/<str:pk>/', login_required(views.Notas_ExtraDetailView.as_view()), name='class_notas_extra_detail'),
    path('lista_notasExtra/paciente/<str:pk>', login_required(views.lista_notas_extra), name="lista_notas_extra"),
    path('notaExtra/<str:pk>/', login_required(views.Notas_EXtraUpdateView.as_view()), name='class_update_notas_extra'),

    path('prueba/<int:pk>/', login_required(views.prueba), name='prueba'),

    path('calendario/', login_required(views.get_first_element), name='calendario'),

    ]
