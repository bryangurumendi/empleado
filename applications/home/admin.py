from django.contrib import admin
from .models import Prueba

# Register your models here.


class PruebaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'subtitulo',
        'cantidad',
    )


admin.site.register(Prueba, PruebaAdmin)
