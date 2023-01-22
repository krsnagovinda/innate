from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from persona import views
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [

     path('lista_usuarios/', login_required(views.index), name='class_personas_lista'),
     path('buscar_usuario/', views.SearchResultsView.as_view(), name='search_results_user'),

     path('quiropracticos_lista/', login_required(views.quiro3), name='class_quiro_lista'),
     path('asistentes_lista/', login_required(views.asistente), name='class_asistente_lista'),
     path('radiologos_lista/', login_required(views.radiologo), name='class_radio_lista'),
     path('capacitacion_lista/', login_required(views.capa), name='class_cap_lista'),
     path('contabilidad_lista/', login_required(views.contable), name='class_conta_lista'),
     path('administradores_lista/', login_required(views.admins), name='class_admins_lista'),

     path('upload_usuario/', login_required(views.UploadPersonaView.as_view()), name='class_upload_persona'),
     
     path('usuario/<int:pk>/', login_required(views.PersonaDetailView.as_view()), name='class_detail_persona'),

     path('delete_usuario/<str:pk>/', login_required(views.PersonaDeleteView.as_view()), name='class_delete_persona'),
     path('update_usuario/<str:pk>/', login_required(views.PersonaUpdateView.as_view()), name='class_update_persona'),

     ]
