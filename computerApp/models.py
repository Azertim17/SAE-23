from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Machine(models.Model):
    
    TYPE = (
        ('PC',('PC - Run windows')),
        ('Mac', ('MAc - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),  
    )
    
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom= models.CharField(
                max_length=6)
    
    maintenanceDate = models.DateField(default = now())
    
    mach = models.CharField(max_length=32, choices=TYPE, default ='PC')

class Personnel(models.Model):
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom = models.CharField(
                max_length=20)
    
    prenom= models.CharField(
                    max_length=20)


    def __str__(self):
        return str(self.id) + "->" + self.nom + " " + self.prenom

    def get_name(self):
        return str(self.id) + "->" + self.nom + " " + self.prenom


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()