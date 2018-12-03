"""parkapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from backoffice.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    # URL pais
    path('pais/add/', pais_add, name='pais_add'),
    path('pais/list/', pais_list, name='pais_list'),
    path('pais/edit/<int:pk>', pais_edit, name='pais_edit'),
    path('pais/delete/<int:pk>', pais_delete, name='pais_delete'),
    path('pais/detail/<int:pk>', pais_detail, name='pais_detail'),


    # URLs departamento

    path('departamento/add/', departamento_add, name='departamento_add'),
    path('departamento/list/', departamento_list, name='departamento_list'),
    path('departamento/edit/<int:pk>', departamento_edit, name='departamento_edit'),
    path('departamento/delete/<int:pk>', departamento_delete, name='departamento_delete'),
    path('departamento/detail/<int:pk>', departamento_detail, name='departamento_detail'),


    # URLs departamento

    path('provincia/add/', provincia_add, name='provincia_add'),
    path('provincia/list/', provincia_list, name='provincia_list'),
    path('provincia/edit/<int:pk>', provincia_edit, name='provincia_edit'),
    path('provincia/delete/<int:pk>', provincia_delete, name='provincia_delete'),
    path('provincia/detail/<int:pk>', provincia_detail, name='provincia_detail'),


    # URLs distrito

    path('distrito/add/', distrito_add, name='distrito_add'),
    path('distrito/list/', distrito_list, name='distrito_list'),
    path('distrito/edit/<int:pk>', distrito_edit, name='distrito_edit'),
    path('distrito/delete/<int:pk>', distrito_delete, name='distrito_delete'),
    path('distrito/detail/<int:pk>', distrito_detail, name='distrito_detail'),


    # URLs estacionamiento

    path('estacionamiento/add/', estacionamiento_add, name='estacionamiento_add'),
    path('estacionamiento/list/', estacionamiento_list, name='estacionamiento_list'),
    path('estacionamiento/edit/<int:pk>', estacionamiento_edit, name='estacionamiento_edit'),
    path('estacionamiento/delete/<int:pk>', estacionamiento_delete, name='estacionamiento_delete'),
    path('estacionamiento/detail/<int:pk>', estacionamiento_detail, name='estacionamiento_detail'),

]
