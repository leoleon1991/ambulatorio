from django.conf.urls import url
from apps.medicamento.views import index_medicamento, medicamento_view, medicamento_list, medicamento_edit, medicamento_delete

urlpatterns = [
	url(r'^$', index_medicamento),
	url(r'^registrar/$', medicamento_view, name='medicamento_registrar'),
	url(r'^listar/$', medicamento_list, name='medicamento_listar'),
	url(r'^editar/(?P<id_medicamento>\d+)/$', medicamento_edit, name='medicamento_editar'),
	url(r'^eliminar/(?P<id_medicamento>\d+)/$', medicamento_delete, name='medicamento_eliminar'),
]