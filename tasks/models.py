from django.db import models

# Create your models here.

class Jurisprudencias(models.Model):
    tipoCausa= models.CharField(max_length=500)
    rol= models.CharField(max_length=500)
    caratula= models.CharField(max_length=500)
    nombreProyecto = models.CharField(max_length=500)
    descriptores = models.CharField(max_length=500)