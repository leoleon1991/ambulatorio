from django.conf.urls import url
from apps.medico.views import index_medico, medico_view, medico_list, medico_edit, medico_delete

urlpatterns = [
	url(r'^$', index_medico, name='index_medico'),
	url(r'^registrar/$', medico_view, name='medico_registrar'),
	url(r'^listar/$', medico_list, name='medico_listar'),
	url(r'^editar/(?P<id_medico>\d+)/$', medico_edit, name='medico_editar'),
	url(r'^eliminar/(?P<id_medico>\d+)/$', medico_delete, name='medico_eliminar'),
]