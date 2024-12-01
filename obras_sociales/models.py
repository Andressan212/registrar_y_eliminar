# obras_sociales/models.py
from django.db import models

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre
