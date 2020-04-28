from django.shortcuts import render
from django.views.generic.edit import (
    FormView,
)
from django.views.generic import (
    ListView,
)

from .models import Departamento
from applications.persona.models import Empleado
from .forms import NewDepartamentoForm

# Create your views here.

from .forms import NewDepartamentoForm


# Lista de Departamentos

class ListAllDepartamentos(ListView):
    template_name = "departamento/listar_departamentos.html"
    model = Departamento
    context_object_name = 'lista'
    paginate_by = 5

    def get_queryset(self):
        palabra = self.request.GET.get('KeyWord', '')
        lista = Departamento.objects.filter(
            name__icontains=palabra
        )
        return lista


class NewDepartamentoView(FormView):
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = 'departamento_app:listar-departamentos'

    def form_valid(self, form):

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa,
        )

        return super(NewDepartamentoView, self).form_valid(form)
