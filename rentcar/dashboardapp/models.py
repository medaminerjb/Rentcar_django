from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

class ModuleVoiture(models.Model):
    id_module = models.AutoField(primary_key=True)
    name_module = models.CharField(max_length=255,null=False)
    marque = models.CharField(max_length=63,null=False)
    puissance = models.IntegerField(max_length=2,null=True)
    nbr_place = models.IntegerField(max_length=2,null=True)
    reservoir = models.IntegerField(max_length=7,null=True)
    prix_neuf = models.IntegerField(max_length=11,null=True)
    etat = models.CharField(max_length=5,null=False,default='neuf')
    desponiblte = models.CharField(max_length=55,null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return str(self.name_module)
class voiture(models.Model):
    id = models.AutoField(primary_key=True)
    numeroMat = models.CharField(max_length=127, unique=True)
    modulecar = models.CharField(max_length=127)
    couleur = models.CharField(max_length=63)
    type = models.CharField(max_length=63)
    modulevoiture = models.ForeignKey(ModuleVoiture,blank=True,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.numeroMat)
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127,null=False)
    email = models.EmailField(null=True)
    numerotel = models.IntegerField(max_length=8,null=True)
    user= models.ForeignKey(User,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
class agent(models.Model):
    id_agent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127,null=False)
    email = models.EmailField(null=True)
    numerotel = models.IntegerField(max_length=8,null=True)
    user= models.ForeignKey(User)
    def __str__(self):
        return str(self.name)

class reservation(models.Model):
    id_reservation = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    place = models.CharField(blank=True,null=True)
    status = models.CharField(blank=True,null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    date_reservation = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client,blank=True,on_delete=models.CASCADE)
    voiture = models.ForeignKey(voiture,blank=True,on_delete=models.CASCADE)
    numero_tel = models.IntegerField(max_length=8,null=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return str(self.id_reservation)
class sous_traitance(models.Model):
    id_sous_traitance = models.AutoField(primary_key=True)
    taux_echeance = models.IntegerField(max_length=11,blank=True,null=True)
    number_echeance = models.IntegerField(max_length=4,null=True)
    number_echance_paier = models.IntegerField(max_length=4,null=True)
    avance = models.IntegerField(max_length=11,null=True)
    date_paiment = models.DateField(blank=True,null=True)
    date_debut = models.DateField(blank=True,null=True)
    date_fin = models.DateField(blank=True,null=True)
    voiture = models.ForeignKey(voiture,blank=True,on_delete=models.CASCADE)
    agent = models.ForeignKey(agent,blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id_sous_traitance)

class historique_st(models.Model):
    id_echeance = models.AutoField(primary_key=True)
    echeance = models.IntegerField(max_length=11,null=True)
    date_paiment = models.DateField(blank=True,null=True)
    staut = models.CharField(blank=True,null=True)
    sous_traitance = models.ForeignKey(sous_traitance,blank=True,on_delete=models.CASCADE)
    voiture = models.ForeignKey(voiture,blank=True,on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return str(self.id_echeance)


    


    