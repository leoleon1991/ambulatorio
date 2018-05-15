from django.conf.urls import url
from apps.medico.views import index_medico, medico_view, medico_list, medico_edit, medico_delete, \
	MedicoList, MedicoCreate, MedicoUpdate, MedicoDelete

urlpatterns = [
	url(r'^$', index_medico, name='index_medico'),
	url(r'^registrar/$', MedicoCreate.as_view(), name='medico_registrar'),
	url(r'^listar/$', MedicoList.as_view(), name='medico_listar'),
	url(r'^editar/(?P<pk>\d+)/$', MedicoUpdate.as_view(), name='medico_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', MedicoDelete.as_view(), name='medico_eliminar'),
]