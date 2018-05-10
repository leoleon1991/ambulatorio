from django.shortcuts import render, redirect	
from django.http import HttpResponse
from apps.consulta.forms import ConsultaForm
from apps.consulta.models import Consulta

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
	consulta = Consulta.objects.all()
	contexto = {'consultas': consulta}
	return render(request, 'consulta/consulta_list.html', contexto)

