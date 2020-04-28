from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado
from django.urls import reverse_lazy

from .forms import EmpleadoForm

'''-------------------------------------------------------------------------'''


# Pagina de inicio


class StartView(TemplateView):
    template_name = 'inicio.html'


'''------------------------------------------------------------------------'''


# Lista de empleados


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado  # enviamos todo los registros de la tabla empleados.
    context_object_name = 'lista'
    paginate_by = 5

    def get_queryset(self):
        key_word = self.request.GET.get('KeyWord', '')
        lista = Empleado.objects.filter(
            full_name__icontains=key_word
        )
        return lista


'''------------------------------------------------------------------------'''


# Detalle de un empleado.


class EmpleadoDetailView(DetailView):
    template_name = "persona/detail_empleado.html"
    model = Empleado
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'EMPLEADO DEL MES'
        return context


'''------------------------------------------------------------------------'''


# Lista de empleados, filtrando por departamento.


class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_area.html'
    context_object_name = 'lista_departamento'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista


'''------------------------------------------------------------------------'''
# ADMINISTRAR EMPLEADO

# Administrar empleado -> LISTAR


class AdminListAllEmpleados(ListView):
    template_name = 'persona/administrar_empleados.html'
    model = Empleado  # enviamos todo los registros de la tabla empleados.
    context_object_name = 'lista'
    paginate_by = 10


# Administrar empleado -> MODIFICAR


class UpdateEmpleado(UpdateView):
    model = Empleado
    template_name = "persona/modificar.html"
    context_object_name = "empleado"
    fields = [  # Se puede usar (__all__)
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:administrar-empleados')


"""def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().post(request, *args, **kwargs)


def form_valid(self, form):
    empleados = form.save()
    empleados.full_name = empleados.first_name + ' ' + empleados.last_name
    empleados.save()
    return super(EmpleadoUpdateView, self).form_valid(form)"""


# Administrar empleado -> ELIMINAR


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/eliminar.html"
    context_object_name = "empleado"
    success_url = reverse_lazy('persona_app:administrar-empleados')


'''------------------------------------------------------------------------'''


"""                 LISTA DE ENMPLEADOS POR HABILIDADES DE EMPLEADO
                                        |
                                        |
                                        v                                   """


class ListHabilityEmpleado(ListView):
    template_name = 'persona/list_habilidad.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
        return empleado.habilidades.all()


# Crear empleado


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:listar-empleados')

    # funcion que permite guardar los datos y poder hacer cosas adicionales con esos datos antes de volver a guardar.
    def form_valid(self, form):
        empleados = form.save()
        empleados.full_name = empleados.first_name + ' ' + empleados.last_name
        empleados.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    # crear empleado con formulario personalizado
