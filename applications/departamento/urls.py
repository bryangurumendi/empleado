from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path(
        'listar-departamentos/',
        views.ListAllDepartamentos.as_view(),
        name='listar-departamentos',
    ),

    path(
        'new-departamento/',
        views.NewDepartamentoView.as_view(),
        name='new-departamento',
    ),
]
