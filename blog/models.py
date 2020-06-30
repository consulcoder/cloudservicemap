from django.db import models
from django.utils import *


class Categorie(models.Model):
    nom_cat = models.CharField(max_length=30, verbose_name='Nom Categorie')

    class Meta:
        verbose_name = "Categorie"

    def __str__(self):
        return self.nom_cat


class Sous_Categorie(models.Model):
    nom_s_cat = models.CharField(max_length=100, verbose_name='Nom Souscategorie')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sous-Categorie"
        ordering = ["-nom_s_cat"]

    def __str__(self):
        return self.nom_s_cat


class Service(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="../static", null='False')
    fournisseurs = models.CharField(max_length=255, blank=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    statut = models.BooleanField(default=True)
    sous_categorie = models.ForeignKey(Sous_Categorie, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Service"

    def __str__(self):
        return self.nom


class Fournisseur(models.Model):
    nom_f = models.CharField(max_length=100, verbose_name='Nom Fournisseur')
    image = models.ImageField(upload_to="../static", null='False')
    services = models.ManyToManyField(Service)

    class Meta:
        verbose_name = "Fournisseur" #(verbose_name is a human-readable name for the field especially in Django Administration)

    def __str__(self):
        return self.nom_f