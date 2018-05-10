from django import forms
from apps.medico.models import Medico

class MedicoForm(forms.ModelForm):

	class Meta:
		model = Medico

		fields = [
			'nombre',
			'apellido',
			'cedula',
			]

		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'cedula': 'Cedula de Identidad',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),	
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'cedula': forms.TextInput(attrs={'class':'form-control'}),
		}