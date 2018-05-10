from django.db import models
from apps.paciente.models import Paciente
from apps.medico.models import Medico

# Create your models here.

class Consulta(models.Model):
	paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	fecha_consulta = models.DateField()
	hora_consulta = models.TimeField()
	medico_asignado = models.ForeignKey(Medico, null=True, blank=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return '{} {}'.format(self.paciente.nombres, self.paciente.apellidos)
