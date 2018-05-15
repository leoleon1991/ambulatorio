from django import forms
from apps.consulta.models import Consulta
from django.contrib.admin import widgets

class ConsultaForm(forms.ModelForm):

	class Meta:
		model = Consulta

		fields = [
			'paciente',
			'fecha_consulta',
			'hora_consulta',
			'medico_asignado',
			]

		labels = {
			'paciente': 'Paciente',
			'fecha_consulta': 'Fecha de la Consulta (DD-MM-YYYY)',
			'hora_consulta': 'Hora de la Consulta (HH:MM)',
			'medico_asignado': 'Medico asignado para la Consulta',
		}

		widgets = {
			'paciente': forms.Select(attrs={'class':'form-control'}),
			'fecha_consulta': forms.TextInput(attrs={'class':'form-control'}),
			'hora_consulta': forms.TextInput(attrs={'class':'form-control'}),
			'medico_asignado': forms.Select(attrs={'class':'form-control'}),
		}