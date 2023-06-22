from django.db import models

# Create your models here.

class Jurisprudencias(models.Model):
    tipoCausa= models.CharField(max_length=500)
    rol= models.CharField(max_length=500)
    caratula= models.CharField(max_length=500)
    nombreProyecto = models.CharField(max_length=500)
    descriptores = models.CharField(max_length=500)

class ConcesionesVigentes(models.Model):
    numeroConcesion = models.IntegerField(),
    tipoDeConcesion = models.CharField(max_length=250),
    comuna = models.CharField(max_length=250),
    lugar = models.CharField(max_length=500),
    rsDs = models.CharField(max_length=250),
    tipoTramite = models.CharField(max_length=250),
    tipoVigencia = models.CharField(max_length=250)