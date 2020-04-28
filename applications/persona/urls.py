from . import views
from django.contrib import admin
from django.urls import path

app_name = 'persona_app'

urlpatterns = [
    # PAGINA DE INICIO
    path(
        '',
        views.StartView.as_view(),
        name='inicio',
    ),

    # LISTA DE TODOS LOS EMPLEADOS
    path(
        'listar-empleados/',
        views.ListAllEmpleados.as_view(),
        name='listar-empleados',
    ),

    # DETALLE DE UN EMPLEADO
    path(
        'detallar-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='detallar-empleado',
    ),

    # LISTA DE EMPLEADO POR DEPARTAMENTO
    path(
        'listar-por-departamento/<name>/',
        views.ListByAreaEmpleado.as_view(),
        name='empleados_departamento',
    ),

    # LISTA DE EMPLEADOS PARA ADMINISTRAR
    path(
        'administrar-empleados/',
        views.AdminListAllEmpleados.as_view(),
        name='administrar-empleados',
    ),

    # CREAR UN EMPLEADO
    path(
        'crear-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='crear-empleado',
    ),

    # MODIFICAR UN EMPLEADO
    path(
        'modificar-empleado/<pk>/',
        views.UpdateEmpleado.as_view(),
        name='modificar-empleado',
    ),

    # ELIMINAR UN EMPLEADO
    path(
        'eliminar-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado',
    ),

    path('listar-por-habilidad/',
         views.ListHabilityEmpleado.as_view()),
]
