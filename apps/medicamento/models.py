from django.db import models
# Create your models here.

class Medicamento(models.Model):
	nombre = models.CharField(max_length=20)
	presentacion = models.CharField(max_length=10)
	via = models.CharField(max_length=10)
	cantidad = models.IntegerField()
	fecha_elaboracion = models.DateField()
	fecha_vencimiento = models.DateField()	

	def __str__(self):
		return self.nombre