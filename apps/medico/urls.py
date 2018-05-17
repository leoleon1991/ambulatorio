from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.medico.views import index_medico, medico_view, medico_list, medico_edit, medico_delete, \
	MedicoList, MedicoCreate, MedicoUpdate, MedicoDelete

urlpatterns = [
	url(r'^$', login_required(index_medico), name='index_medico'),
	url(r'^registrar/$', login_required(MedicoCreate.as_view()), name='medico_registrar'),
	url(r'^listar/$', login_required(MedicoList.as_view()), name='medico_listar'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(MedicoUpdate.as_view()), name='medico_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(MedicoDelete.as_view()), name='medico_eliminar'),
]