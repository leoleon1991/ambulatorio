from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from apps.paciente.forms import PacienteForm, AreaForm
from django.views.generic import CreateView
from apps.paciente.models import Paciente, Area

# Create your views here.

def index_paciente(request):
	return render(request, 'paciente/index_paciente.html')

def paciente_view(request):
	if request.method == 'POST':
		form = PacienteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('paciente:paciente_listar')
	else:
		form = PacienteForm()
	return render(request, 'paciente/paciente_form.html', {'form': form})

def area_view(request):
	if request.method == 'POST':
		form = AreaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('paciente:area_listar')
	else:
		form = AreaForm()
	return render(request, 'paciente/area_form.html', {'form': form})

def paciente_list(request):
	paciente = Paciente.objects.all().order_by('id')
	contexto = {'pacientes': paciente}
	return render(request, 'paciente/paciente_list.html', contexto)

def area_list(request):
	area = Area.objects.all().order_by('id')
	contexto = {'areas': area}
	return render(request, 'paciente/area_list.html', contexto)

def paciente_edit(request, id_paciente):
	paciente = Paciente.objects.get(id=id_paciente)
	if request.method == 'GET':
		form = PacienteForm(instance=paciente)
	else:
		form = PacienteForm(request.POST, instance=paciente)
		if form.is_valid():
			form.save()
		return redirect('paciente:paciente_listar')
	return render(request, 'paciente/paciente_form.html', {'form':form})

def area_edit(request, id_area):
	area = Area.objects.get(id=id_area)
	if request.method == 'GET':
		form = AreaForm(instance=area)
	else:
		form = AreaForm(request.POST, instance=area)
		if form.is_valid():
			form.save()
		return redirect('paciente:area_listar')
	return render(request, 'paciente/area_form.html', {'form': form})

def paciente_delete(request, id_paciente):
	paciente = Paciente.objects.get(id=id_paciente)
	if request.method == 'POST':
		paciente.delete()
		return redirect('paciente:paciente_listar')
	return render(request, 'paciente/paciente_delete.html', {'paciente':paciente})

def area_delete(request, id_area):
	area = Area.objects.get(id=id_area)
	if request.method == 'POST':
		area.delete()
		return redirect('paciente:area_listar')
	return render(request, 'paciente/area_delete.html', {'area':area})