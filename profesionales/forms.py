from django import forms
from .models import profesionale

class DateInput(forms.DateInput):
    input_type = 'date'


class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = profesionale
        fields = ['rut_profesional', 'nombres','apellidos', 'fecha_nac', 'direccion', 'num_casa', 'telefono',
                  'email','profesion']
        labels = {
            'rut_profesional': 'Rut del profesional',
            'nombres': 'Nombres del profesional',
            'apellidos': 'Apellidos',
            'fecha_nac': 'Fecha de nacimiento',
            'direccion': 'Dirección',
            'num_casa': 'Numero de Casa',
            'telefono': 'Telefono',
            'email': 'E-mail',
            'profesion': 'Profesion ',
        }
        widgets = {
            'rut_profesional': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese rut del profesional',
                    'id': 'rut_profesional'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombres del profesional',
                    'id': 'nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese apellidos del profesional',
                    'id': 'apellidos'
                }
            ),
            'fecha_nac': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha_nac'
                },
                years=range(1930, 2030)
            ),

            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion del profesional',
                    'id': 'direccion'
                }
            ),
            'num_casa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese numero de casa del profesional',
                    'id': 'num_casa'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono del profesional',
                    'id': 'telefono'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese E-mail del profesional',
                    'id': 'email'
                }
            ),
            'profesion': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese profesion',
                    'id': 'profesion'
                }
            ),
        }