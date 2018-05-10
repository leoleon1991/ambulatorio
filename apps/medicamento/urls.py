from django.conf.urls import url
from apps.medicamento.views import index_medicamento, medicamento_view, medicamento_list

urlpatterns = [
	url(r'^$', index_medicamento),
	url(r'^registrar/$', medicamento_view, name='medicamento_registrar'),
	url(r'^listar/$', medicamento_list, name='medicamento_listar'),
]