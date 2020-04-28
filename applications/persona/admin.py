from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades', 'departamento')

    filter_horizontal = ('habilidades',)


class HabilidadesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'habilidad',
    )


admin.site.register(Habilidades, HabilidadesAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
