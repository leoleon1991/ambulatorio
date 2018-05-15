from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from apps.medicamento.forms import MedicamentoForm
from apps.medicamento.models import Medicamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
	medicamento = Medicamento.objects.all().order_by('id')
	contexto = {'medicamentos': medicamento}
	return render(request, 'medicamento/medicamento_list.html', contexto)

def medicamento_edit(request, id_medicamento):
	medicamento = Medicamento.objects.get(id=id_medicamento)
	if request.method == 'GET':
		form = MedicamentoForm(instance=medicamento)
	else: 
		form = MedicamentoForm(request.POST, instance=medicamento)
		if form.is_valid():
			form.save()
		return redirect('medicamento:medicamento_listar')
	return render(request, 'medicamento/medicamento_form.html', {'form': form})

def medicamento_delete(request, id_medicamento):
	medicamento = Medicamento.objects.get(id=id_medicamento)
	if request.method == 'POST':
		medicamento.delete()
		return redirect('medicamento:medicamento_listar')
	return render(request, 'medicamento/medicamento_delete.html', {'medicamento': medicamento})

class MedicamentoList(ListView):
	model = Medicamento
	template_name = 'medicamento/medicamento_list.html'
	#paginate_by = 5

class MedicamentoCreate(CreateView):
	model = Medicamento
	form_class = MedicamentoForm
	template_name = 'medicamento/medicamento_form.html'
	succes_url = reverse_lazy('medicamento:medicamento_listar')

class MedicamentoUpdate(UpdateView):
	model = Medicamento
	form_class = MedicamentoForm
	template_name = 'medicamento/medicamento_form.html'
	succes_url = reverse_lazy('medicamento:medicamento_listar')

class MedicamentoDelete(DeleteView):
	model = Medicamento
	template_name = 'medicamento/medicamento_delete.html'
	succes_url = reverse_lazy('medicamento:medicamento_listar')

