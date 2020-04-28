from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',

        )
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Su nombre',
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 10:
            raise forms.ValidationError(
                "DEBE INGRESAR NUMEROS MAYORES A 10")
        return cantidad
