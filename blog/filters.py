from django.contrib.auth.models import User
import django_filters
from .models import Categorie, Sous_Categorie


class CategorieFilter(django_filters.FilterSet):
    class Meta:
        model = Categorie
        fields = ['nom_cat']


class Sous_CategorieFilter(django_filters.FilterSet):
    class Meta:
        model = Sous_Categorie
        fields = ['nom_s_cat']
