from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.paciente.views import index_paciente, paciente_view, area_view, paciente_list, \
	area_list, paciente_edit, area_edit, paciente_delete, area_delete, PacienteList, AreaList, \
    PacienteCreate, AreaCreate, PacienteUpdate, AreaUpdate, PacienteDelete

urlpatterns = [
    url(r'^$', index_paciente, name='index_paciente'),
    url(r'^registrar_paciente/$', PacienteCreate.as_view(), name='paciente_registrar'),
    url(r'^registrar_area/$', AreaCreate.as_view(), name='area_registrar'),
    url(r'^listar_pacientes/$', PacienteList.as_view(), name='paciente_listar'),
    url(r'^listar_areas/$', AreaList.as_view(), name='area_listar'),
    url(r'^editar_paciente/(?P<pk>\d+)/$', PacienteUpdate.as_view(), name='paciente_editar'),
    url(r'^editar_area/(?P<pk>\d+)/$', AreaUpdate.as_view(), name='area_editar'),
    url(r'^eliminar_paciente/(?P<pk>\d+)/$', PacienteDelete.as_view(), name='paciente_eliminar'),
    url(r'^eliminar_area/(?P<id_area>\d+)/$', area_delete, name='area_eliminar'),
]
