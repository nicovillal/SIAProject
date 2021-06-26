from django import forms
from .models import ficha


class FichaForm(forms.ModelForm):
    class Meta:
        model = ficha
        fields = ['paciente', 'profesional','diagnostico', 'tratamiento', 'costo', 'receta', 'fecha',
                  'hora']
        labels = {
            'paciente': 'Paciente',
            'profesional': 'Profesional',
            'diagnostico': 'Diagnostico',
            'tratamiento': 'Tratamiento',
            'costo': 'Costo',
            'receta': 'Receta',
            'fecha': 'Fecha',
            'hora': 'Hora',
        }
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Paciente',
                    'id': 'paciente'
                }
            ),
            'profesional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Profesional',
                    'id': 'profesional'
                }
            ),
            'diagnostico': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Diagnostico',
                    'id': 'diagnostico'
                }
            ),
            'tratamiento': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Tratamiento',
                    'id': 'tratamiento'
                }
            ),
            'costo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Costo',
                    'id': 'costo'
                }
            ),
            'receta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Receta',
                    'id': 'receta'
                }
            ),
            'fecha': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Fecha',
                    'id': 'fecha'
                }
            ),
            'hora': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Hora',
                    'id': 'hora'
                }
            ),
        }