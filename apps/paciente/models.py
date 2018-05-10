from django.db import models
# Create your models here.

class Area(models.Model):
	nombre = models.CharField(max_length=20)
	ubicacion = models.CharField(max_length=20)
	jefe = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre

class Paciente(models.Model):
	GENEROS = (
		('F', 'Femenino'),
		('M', 'Masculino'),
		('I', 'Indefinido')
	)

	FUMA = (
		('S', 'Si'),
		('N', 'No'),
	)
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	cedula = models.CharField(max_length=8)
	fecha_nacimiento = models.DateField()
	edad = models.IntegerField()
	genero = models.CharField(max_length=1, choices=GENEROS)
	tipo_sangre = models.CharField(max_length=5)
	telefono = models.CharField(max_length=11)
	correo = models.EmailField()
	fumador = models.CharField(max_length=1, choices=FUMA)
	alergico = models.CharField(max_length=20)
	motivo = models.CharField(max_length=50)
	area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)




		