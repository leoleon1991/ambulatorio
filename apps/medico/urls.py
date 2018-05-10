from django.conf.urls import url
from apps.medico.views import index_medico, medico_view, medico_list

urlpatterns = [
	url(r'^$', index_medico, name='index_medico'),
	url(r'^registrar/$', medico_view, name='medico_registrar'),
	url(r'^listar/$', medico_list, name='medico_listar'),
]