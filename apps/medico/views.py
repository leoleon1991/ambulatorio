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
	medico = Medico.objects.all()
	contexto = {'medicos': medico}
	return render(request, 'medico/medico_list.html', contexto)