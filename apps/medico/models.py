from django.db import models

# Create your models here.

class Medico(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	cedula = models.CharField(max_length=8)	

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)