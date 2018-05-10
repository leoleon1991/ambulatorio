from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.paciente.views import index_paciente, paciente_view, area_view, paciente_list, area_list

urlpatterns = [
    url(r'^$', index_paciente, name='index_paciente'),
    url(r'^registrar_paciente/$', paciente_view, name='paciente_registrar'),
    url(r'^registrar_area/$', area_view, name='area_registrar'),
    url(r'^listar_pacientes/$', paciente_list, name='paciente_listar'),
    url(r'^listar_areas/$', area_list, name='area_listar'),
]
