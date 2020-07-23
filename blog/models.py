from django.db import models
from django.utils import *
from cropperjs.models import CropperImageField
import Cloud_Service_Map.utils as utils


class Categorie(models.Model):
    nom_cat = models.CharField(max_length=30, verbose_name='Nom Categorie')

    class Meta:
        verbose_name = "Categorie"

    def toArray(self):
        return {
            'id': self.pk,
            'name': self.__str__()
        }

    def __str__(self):
        return self.nom_cat


class Sous_Categorie(models.Model):
    nom_s_cat = models.CharField(max_length=100, verbose_name='Nom Souscategorie')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sous-Categorie"
        ordering = ["-nom_s_cat"]

    def toArray(self):
        return {
            'id': self.pk,
            'name': self.__str__()
        }

    def __str__(self):
        return self.nom_s_cat


class Service(models.Model):
    nom = models.CharField(max_length=255, verbose_name='Nom Service')
    image = CropperImageField(upload_to=utils.RELATIVE_STATIC_URL, null='False',dimensions=(200,200))
    fournisseurs = models.CharField(max_length=255, blank=False, verbose_name='Fournisseur')
    url = models.URLField(max_length=200, null=True, blank=True)
    statut = models.BooleanField(default=True)
    sous_categorie = models.ForeignKey(Sous_Categorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Service"

    def toArray(self):
        return {
            'id': self.pk,
            'name': self.__str__(),
            'image': self.image.url,
            'url': self.url,
        }

    def __str__(self):
        return self.nom


class Fournisseur(models.Model):
    nom_f = models.CharField(max_length=100, verbose_name='Nom Fournisseur', null=True, blank=True)
    image = CropperImageField(upload_to=utils.RELATIVE_STATIC_URL, null='False',dimensions=(200,200))
    services = models.ManyToManyField(Service)

    class Meta:
        verbose_name = "Fournisseur"  # (verbose_name is a human-readable name for the field especially in Django Administration)
        

    def toArray(self):
        return {
            'id': self.pk,
            'name': self.__str__(),
            'image': self.image.url,
        }
#GGGGf