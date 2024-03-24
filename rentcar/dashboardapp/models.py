from django.db import models
from django.contrib.auth.models import User

class Voiture(models.Model):
    id = models.AutoField(primary_key=True)
    numeroMat = models.CharField(max_length=100, unique=True)
    modulecar = models.CharField(max_length=100)
    couleur = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    def __str__(self):
        return str(self.numeroSerie)