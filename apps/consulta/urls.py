from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.consulta.views import index_consulta, consulta_view, consulta_list, consulta_edit, \
	consulta_delete, ConsultaList, ConsultaCreate, ConsultaUpdate, ConsultaDelete

urlpatterns = [
	url(r'^$', login_required(index_consulta)),
	url(r'^registrar/$', login_required(ConsultaCreate.as_view()), name="consulta_registrar"),
	url(r'^listar/$', login_required(ConsultaList.as_view()), name="consulta_listar"),
	url(r'^editar/(?P<pk>\d+)/$', login_required(ConsultaUpdate.as_view()), name="consulta_editar"),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(ConsultaDelete.as_view()), name="consulta_eliminar"),
]