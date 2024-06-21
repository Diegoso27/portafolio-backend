from django.db import models
from django.contrib.auth.models import User

class Infante(models.Model):

    child_name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    rut = models.CharField(max_length=15, null=True)
    blood_type = models.CharField(max_length=50)
    diagnostic = models.CharField(max_length=100)
    prevision = models.CharField(max_length=50, null=True)
    alergias = models.CharField(max_length=200, null=True)
    antecendetes_medicos = models.CharField(max_length=300, null=True)

class Servicios_emergencia(models.Model):

    numero_bomberos = models.CharField(max_length=50)
    numero_carabineros = models.CharField(max_length=50)
    numero_asistencia_medica = models.CharField(max_length=50)


class Propiedad(models.Model):

    owner = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    infantes = models.ManyToManyField(Infante, related_name='infante_propiedad', blank=True)  
    asistente = models.ManyToManyField(User, related_name='asistente_propiedad', blank=True)
    servicios_emergencia = models.ManyToManyField(Servicios_emergencia, related_name='servicios_propiedad', blank=True)
    





