from django.db import models

# Create your models here.

class Fechas(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_nacimiento = models.DateField()