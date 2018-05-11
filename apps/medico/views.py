from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.medico.forms import MedicoForm
from apps.medico.models import Medico

# Create your views here.

def index_medico(request):
	return HttpResponse("Esta es la pagina para la aplicacion Medico")

def medico_view(request):
	if request.method == 'POST':
		form = MedicoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('medico:medico_listar')
	else:
		form = MedicoForm()
	return render(request, 'medico/medico_form.html', {'form': form})

def medico_list(request):
	medico = Medico.objects.all().order_by('id')
	contexto = {'medicos': medico}
	return render(request, 'medico/medico_list.html', contexto)

def medico_edit(request, id_medico):
	medico = Medico.objects.get(id=id_medico)
	if request.method == 'GET':
		form = MedicoForm(instance=medico)
	else:
		form = MedicoForm(request.POST, instance=medico)
		if form.is_valid():
			form.save()
		return redirect('medico:medico_listar')
	return render(request, 'medico/medico_form.html', {'form': form})

def medico_delete(request, id_medico):
	medico = Medico.objects.get(id=id_medico)
	if request.method == 'POST':
		medico.delete()
		return redirect('medico:medico_listar')
	return render(request, 'medico/medico_delete.html', {'medico': medico})