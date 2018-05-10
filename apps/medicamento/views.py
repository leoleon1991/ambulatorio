from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.medicamento.forms import MedicamentoForm
from apps.medicamento.models import Medicamento

# Create your views here.

def index_medicamento(request):
	return HttpResponse("Esta es la vista para la aplicacion Medicamento")

def medicamento_view(request):
	if request.method == 'POST':
		form = MedicamentoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('medicamento:medicamento_listar')
	else:
		form = MedicamentoForm()
	return render(request, 'medicamento/medicamento_form.html', {'form': form})

def medicamento_list(request):
	medicamento = Medicamento.objects.all()
	contexto = {'medicamentos': medicamento}
	return render(request, 'medicamento/medicamento_list.html', contexto)
