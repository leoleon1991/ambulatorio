from django.conf.urls import url
from apps.consulta.views import index_consulta, consulta_view, consulta_list, consulta_edit, \
	consulta_delete, ConsultaList, ConsultaCreate, ConsultaUpdate, ConsultaDelete

urlpatterns = [
	url(r'^$', index_consulta),
	url(r'^registrar/$', ConsultaCreate.as_view(), name="consulta_registrar"),
	url(r'^listar/$', ConsultaList.as_view(), name="consulta_listar"),
	url(r'^editar/(?P<pk>\d+)/$', ConsultaUpdate.as_view(), name="consulta_editar"),
	url(r'^eliminar/(?P<pk>\d+)/$', ConsultaDelete.as_view(), name="consulta_eliminar"),
]