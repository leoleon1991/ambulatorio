from django.conf.urls import url
from apps.medicamento.views import index_medicamento, medicamento_view, medicamento_list, \
	medicamento_edit, medicamento_delete, MedicamentoList, MedicamentoCreate, MedicamentoUpdate, \
	MedicamentoDelete

urlpatterns = [
	url(r'^$', index_medicamento),
	url(r'^registrar/$', MedicamentoCreate.as_view(), name='medicamento_registrar'),
	url(r'^listar/$', MedicamentoList.as_view(), name='medicamento_listar'),
	url(r'^editar/(?P<pk>\d+)/$', MedicamentoUpdate.as_view(), name='medicamento_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', MedicamentoDelete.as_view(), name='medicamento_eliminar'),
]