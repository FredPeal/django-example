from django.db import models

class Materias(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True) 

class Estudiantes(models.Model):
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)