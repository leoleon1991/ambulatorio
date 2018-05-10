from django.conf.urls import url
from apps.consulta.views import index_consulta, consulta_view, consulta_list

urlpatterns = [
	url(r'^$', index_consulta),
	url(r'^registrar/$', consulta_view, name="consulta_registrar"),
	url(r'^listar/$', consulta_list, name="consulta_listar"),
]