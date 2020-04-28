from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'habilidad'
        verbose_name_plural = 'habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    # MODELO PARA TABLA EMPLEADO
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('NombreCompleto', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    avatar = models.ImageField(
        upload_to='empleado', blank=True, null=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'empleados'
        ordering = ['first_name']
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return str(self.id) + '.- ' + self.first_name + ' - \'' + self.last_name + '\''
