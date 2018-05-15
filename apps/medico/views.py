from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from apps.medico.forms import MedicoForm
from apps.medico.models import Medico
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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

class MedicoList(ListView):
	model = Medico
	template_name = 'medico/medico_list.html'
	#paginate_by = 5

class MedicoCreate(CreateView):
	model = Medico
	form_class = MedicoForm
	template_name = 'medico/medico_form.html'
	succes_url = reverse_lazy('medico:medico_listar')

class MedicoUpdate(UpdateView):
	model = Medico
	form_class = MedicoForm
	template_name = 'medico/medico_form.html'
	succes_url = reverse_lazy('medico:medico_listar')

class MedicoDelete(DeleteView):
	model = Medico
	template_name = 'medico/medico_delete.html'
	succes_url = reverse_lazy('medico:medico_listar')

