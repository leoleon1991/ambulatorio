from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.paciente.views import index_paciente, paciente_view, area_view, paciente_list
from apps.paciente.views import area_list, paciente_edit, area_edit, paciente_delete, area_delete

urlpatterns = [
    url(r'^$', index_paciente, name='index_paciente'),
    url(r'^registrar_paciente/$', paciente_view, name='paciente_registrar'),
    url(r'^registrar_area/$', area_view, name='area_registrar'),
    url(r'^listar_pacientes/$', paciente_list, name='paciente_listar'),
    url(r'^listar_areas/$', area_list, name='area_listar'),
    url(r'^editar_paciente/(?P<id_paciente>\d+)/$', paciente_edit, name='paciente_editar'),
    url(r'^editar_area/(?P<id_area>\d+)/$', area_edit, name='area_editar'),
    url(r'^eliminar_paciente/(?P<id_paciente>\d+)/$', paciente_delete, name='paciente_eliminar'),
    url(r'^eliminar_area/(?P<id_area>\d+)/$', area_delete, name='area_eliminar'),
]
