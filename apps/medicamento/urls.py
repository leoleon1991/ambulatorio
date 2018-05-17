from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.medicamento.views import index_medicamento, medicamento_view, medicamento_list, \
	medicamento_edit, medicamento_delete, MedicamentoList, MedicamentoCreate, MedicamentoUpdate, \
	MedicamentoDelete

urlpatterns = [
	url(r'^$', login_required(index_medicamento)),
	url(r'^registrar/$', login_required(MedicamentoCreate.as_view()), name='medicamento_registrar'),
	url(r'^listar/$', login_required(MedicamentoList.as_view()), name='medicamento_listar'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(MedicamentoUpdate.as_view()), name='medicamento_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(MedicamentoDelete.as_view()), name='medicamento_eliminar'),
]