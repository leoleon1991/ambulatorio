from django import forms
from apps.paciente.models import Paciente, Area
from django.contrib.admin import widgets
import datetime
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')

class PacienteForm(forms.ModelForm):
	
	class Meta:
		model = Paciente
		fields = [
			'nombres',
			'apellidos',
			'cedula',
			'fecha_nacimiento',
			'edad',
			'genero',
			'tipo_sangre',
			'telefono',
			'correo',
			'fumador',
			'alergico',
			'motivo',
			'area',
			]

		labels = {
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'cedula': 'Cedula',
			'fecha_nacimiento': 'Fecha de Nacimiento',
			'edad': 'Edad',
			'genero': 'Genero',
			'tipo_sangre': 'Tipo de Sangre',
			'telefono': 'Telefono',
			'correo': 'Correo',
			'fumador': '¿Fumador?',
			'alergico': '¿Alergico a algún medicamento?',
			'motivo': 'Motivo de la visita',
			'area': 'Área a ser remitido',
			}

		widgets = {
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'cedula': forms.TextInput(attrs={'class':'form-control'}),
			#'fecha_nacimiento': forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)),
			#'fecha_nacimiento': forms.DateInput(attrs={'class': 'datepicker'}, format='%d/%m/%Y'),
			#'fecha_nacimiento': forms.DateField(required=False,
        	#	widget=forms.DateInput(attrs={'class': 'datepicker'}),
        	#	help_text="Format: YYYY-MM-DD", is_hidden=False),
        	'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'genero': forms.Select(attrs={'class':'form-control'}),
			'tipo_sangre': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
			'fumador': forms.Select(attrs={'class':'form-control'}),
			'alergico': forms.TextInput(attrs={'class':'form-control'}),
			'motivo': forms.TextInput(attrs={'class':'form-control'}),
			'area': forms.Select(attrs={'class':'form-control'}),	
			}

class AreaForm(forms.ModelForm):

	class Meta:
		model = Area
		fields = [
			'nombre',
			'ubicacion',
			'jefe',
			]

		labels = {
			'nombre': 'Nombre del Área',
			'ubicacion': 'Ubicación del Área',
			'jefe': 'Jefe del Área',
			}
		
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'ubicacion': forms.TextInput(attrs={'class':'form-control'}),
			'jefe': forms.TextInput(attrs={'class':'form-control'}),
			}