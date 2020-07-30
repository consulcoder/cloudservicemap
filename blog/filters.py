from django.contrib.auth.models import User
import django_filters
from .models import Categorie


class CategorieFilter(django_filters.FilterSet):

    class Meta:
        model = Categorie
        fields = ['nom_cat']
