from django.db import models

# Create your models here.
class Indicador(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	valor = models.IntegerField()

	def __unicode__ (self):
		return self.nombre