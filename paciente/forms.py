from django import forms
from .models import paciente
class DateInput(forms.DateInput):
    input_type = 'date'




class PacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ['rut_paciente', 'dni_extranjero','nombres', 'apellidos', 'fecha_nac', 'direccion', 'num_casa', 'telefono',
                  'email', 'infomedica']
        labels = {
            'rut_paciente': 'Rut del paciente',
            'dni_extranjero': 'Dni del paciente',
            'nombres': 'Nombres del paciente',
            'apellidos': 'Apellidos',
            'fecha_nac': 'Fecha de nacimiento',
            'direccion': 'Dirección',
            'num_casa': 'Numero de Casa',
            'telefono': 'Telefono',
            'email': 'E-mail',
            'infomedica': 'Información medica',
        }
        widgets = {
            'rut_paciente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese rut del paciente',
                    'id': 'rut_paciente'
                }
            ),
            'dni_extranjero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese dni extrangero',
                    'id': 'dni_extrangero'
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
            'infomedica': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Información medica del paciente',
                    'id': 'infomedica'
                }
            ),
        }