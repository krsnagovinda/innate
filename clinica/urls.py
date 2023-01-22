from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from clinica import views
from django.contrib.auth.decorators import login_required, permission_required

from clinica import views


urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('precios/', views.precios, name='precios'),    
    path('calendario/', login_required(views.get_first_element), name='calendario'),    
    

    #path('upload_clinica/', login_required(views.UploadClinicaView.as_view()), name='class_upload_clinica'),    
    #path('update/<int:pk>/', login_required(views.UpdateClinicaView.as_view()), name='class_update_clinica'),
    ]
