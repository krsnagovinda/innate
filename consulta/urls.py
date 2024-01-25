from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from consulta import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

     path('consulta_lista/', login_required(views.index), name='class_consulta_lista'),
     path('upload_consulta/', login_required(views.UploadConsultaView.as_view()), name='class_upload_consulta'),
     path('lista_consultas/paciente/<int:pk>', login_required(views.detalle), name="lista_consultas"),
     path('detalle/<int:pk>/', login_required(views.ConsultaDetailView.as_view()), name='class_consulta_detail'),
     path('consulta_update/<int:pk>/', login_required(views.ConsultaUpdateView.as_view()), name='class_update_consulta'),
     path('consulta_delete/<int:pk>/', login_required(views.ConsultaDeleteView.as_view()), name='class_delete_consulta'),

     ]
