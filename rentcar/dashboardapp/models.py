from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid


class marquevehicule(models.Model):
    id_marque = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return str(self.name)
    
class ModuleVoiture(models.Model):
    id_module = models.AutoField(primary_key=True)
    name_module = models.CharField(max_length=255,null=False)
    marque = models.CharField(max_length=63,null=True)
    puissance = models.IntegerField(null=True)
    nbr_place = models.IntegerField(null=True)
    reservoir = models.IntegerField(null=True)
    prix_neuf = models.IntegerField(null=True)
    image = models.CharField(max_length=400, blank=True, null=True)
    marque = models.ForeignKey(marquevehicule,blank=True,null=True,on_delete=models.CASCADE)
    etat = models.CharField(max_length=5,null=True,default='neuf')
    desponiblte = models.CharField(max_length=55,null=True)
    type = models.CharField(max_length=63,null=True)

    created = models.DateTimeField(auto_now_add=True,null=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True,null=True, editable=False)

    def __str__(self) -> str:
        return self.name_module
    
class Voiture(models.Model):
    id = models.AutoField(primary_key=True)
    numeroMat = models.CharField(max_length=127, unique=True)
    couleur = models.CharField(max_length=63,null=True)
    status =models.CharField(max_length=255,null=True)
    modulevoiture = models.ForeignKey(ModuleVoiture,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.numeroMat
class Prices(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField(null=True)
    module = models.OneToOneField(ModuleVoiture,blank=True,on_delete=models.CASCADE,unique=True)

    def __int__(self)->int:
        return self.price

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127,null=False)
    email = models.EmailField(null=True)
    numerotel = models.IntegerField(null=True)
    user= models.ForeignKey(User,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
class agent(models.Model):
    id_agent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127,null=False)
    email = models.EmailField(null=True)
    numerotel = models.IntegerField(null=True)
    user= models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

class reservation(models.Model):
    id_reservation = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    place = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255,blank=True,null=True)
    date_debut = models.DateField(blank=True, null=True)
    
    date_fin = models.DateField(blank=True, null=True)
    date_reservation = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client,blank=True,on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture,blank=True,on_delete=models.CASCADE)
    numero_tel = models.IntegerField(null=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return str(self.id_reservation)
class sous_traitance(models.Model):
    id_sous_traitance = models.AutoField(primary_key=True)
    taux_echeance = models.IntegerField(blank=True,null=True)
    number_echeance = models.IntegerField(null=True)
    number_echance_paier = models.IntegerField(null=True)
    avance = models.IntegerField(null=True)
    date_paiment = models.DateField(blank=True,null=True)
    date_debut = models.DateField(blank=True,null=True)
    date_fin = models.DateField(blank=True,null=True)
    voiture = models.ForeignKey(Voiture,blank=True,on_delete=models.CASCADE)
    agent = models.ForeignKey(agent,blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id_sous_traitance)

class historique_st(models.Model):
    id_echeance = models.AutoField(primary_key=True)
    echeance = models.IntegerField(null=True)
    date_paiment = models.DateField(blank=True,null=True)
    staut = models.CharField(max_length=55,blank=True,null=True)
    sous_traitance = models.ForeignKey(sous_traitance,blank=True,on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture,blank=True,on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return str(self.id_echeance)


    


    