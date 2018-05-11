from django.conf.urls import url
from apps.consulta.views import index_consulta, consulta_view, consulta_list, consulta_edit, consulta_delete

urlpatterns = [
	url(r'^$', index_consulta),
	url(r'^registrar/$', consulta_view, name="consulta_registrar"),
	url(r'^listar/$', consulta_list, name="consulta_listar"),
	url(r'^editar/(?P<id_consulta>\d+)/$', consulta_edit, name="consulta_editar"),
	url(r'^eliminar/(?P<id_consulta>\d+)/$', consulta_delete, name="consulta_eliminar"),
]