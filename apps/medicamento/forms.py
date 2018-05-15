from django import forms
from apps.medicamento.models import Medicamento

class MedicamentoForm(forms.ModelForm):

	class Meta:
		model = Medicamento

		fields = [
			'nombre',
			'presentacion',
			'via',
			'cantidad',
			'fecha_elaboracion',
			'fecha_vencimiento',
			]

		labels = {
			'nombre': 'Nombre',
			'presentacion': 'Presentación',
			'via': 'Vía',
			'cantidad': 'Cantidad',
			'fecha_elaboracion': 'Fecha de Elaboración (DD-MM-YYYY)',
			'fecha_vencimiento': 'Fecha de Vencimiento (DD-MM-YYYY)',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'presentacion': forms.TextInput(attrs={'class':'form-control'}),
			'via': forms.TextInput(attrs={'class':'form-control'}),
			'cantidad': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_elaboracion': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_vencimiento': forms.TextInput(attrs={'class':'form-control'}),
		}
