from django import forms
from .models import profesionale


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
                    'placeholder': 'Ingrese nombres del paciente',
                    'id': 'nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese apellidos del paciente',
                    'id': 'apellidos'
                }
            ),
            'fecha_nac': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese fecha nacimiento del paciente',
                    'id': 'fecha_nac'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion del paciente',
                    'id': 'direccion'
                }
            ),
            'num_casa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese numero de casa del paciente',
                    'id': 'num_casa'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono del paciente',
                    'id': 'telefono'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese E-mail del paciente',
                    'id': 'email'
                }
            ),
            'profesion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese profesion',
                    'id': 'profesion'
                }
            ),
        }