from django import forms
from .models import cita

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class CitaForm(forms.ModelForm):
    class Meta:
        model = cita
        fields = ['paciente', 'profesional','fecha_cita','hora_cita', 'estado', 'motivo_anulacion']
        labels = {
            'paciente': 'Paciente',
            'profesional': 'Profesional',
            'fecha_cita': 'Fecha de Cita',
            'hora_cita' : 'Hora de Cita',
            'estado': 'Estado de la Cita',
            'motivo_anulacion': 'Motivo de la anulación',
            }
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Seleccione Paciente',
                    'id': 'paciente'
                }
            ),
            'profesional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccion el Profesional',
                    'id': 'profesional'
                }
            ),
            'fecha_cita': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha_cita'
                }

            ),
            'hora_cita': TimeInput(),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione estado de la Cita',
                    'id': 'estado'
                }
            ),
            'motivo_anulacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Motivo de la anulación',
                    'id': 'motivo_anulacion'
                }
            ),
        }
