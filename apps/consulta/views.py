from django.shortcuts import render, redirect	
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from apps.consulta.forms import ConsultaForm
from apps.consulta.models import Consulta
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def index_consulta(request):
	return HttpResponse("Esta es la vista para la aplicacion Consulta")

def consulta_view(request):
	if request.method == 'POST':
		form = ConsultaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('consulta:consulta_listar')
	else:
		form = ConsultaForm()
	return render(request, 'consulta/consulta_form.html', {'form': form})

def consulta_list(request):
	consulta = Consulta.objects.all().order_by('id')
	contexto = {'consultas': consulta}
	return render(request, 'consulta/consulta_list.html', contexto)

def consulta_edit(request, id_consulta):
	consulta = Consulta.objects.get(id=id_consulta)
	if request.method == 'GET':
		form = ConsultaForm(instance=consulta)
	else:
		form = ConsultaForm(request.POST, instance=consulta)
		if form.is_valid():
			form.save()
		return redirect('consulta:consulta_listar')
	return render(request, 'consulta/consulta_form.html', {'form': form})

def consulta_delete(request, id_consulta):
	consulta = Consulta.objects.get(id=id_consulta)
	if request.method == 'POST':
		consulta.delete()
		return redirect('consulta:consulta_listar')
	return render(request, 'consulta/consulta_delete.html', {'consulta': consulta})

class ConsultaList(ListView):
	model = Consulta
	template_name = 'consulta/consulta_list.html'
	#paginate_by = 5

class ConsultaCreate(CreateView):
	model = Consulta
	form_class = ConsultaForm
	template_name = 'consulta/consulta_form.html'
	succes_url = reverse_lazy('consulta:consulta_listar')

class ConsultaUpdate(UpdateView):
	model = Consulta
	form_class = ConsultaForm
	template_name = 'consulta/consulta_form.html'
	succes_url = reverse_lazy('consulta:consulta_listar')

class ConsultaDelete(DeleteView):
	model = Consulta
	template_name = 'consulta/consulta_delete.html'
	succes_url = reverse_lazy('consulta:consulta_listar')
