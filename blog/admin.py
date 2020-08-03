from django.contrib import admin
from blog.models import Categorie, Sous_Categorie, Service, Fournisseur


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sous_categorie', 'statut', 'fournisseurs', 'url')
    list_filter = ('nom', 'sous_categorie', 'fournisseurs')
    search_fields = ['nom']

    fieldsets = (
        # Fieldset 1 : meta-info (nom)
        ('Général', {
            # 'classes': ['collapse', ],
            'fields': ('nom', 'sous_categorie', 'image', 'statut', 'fournisseurs', 'url')
        }),

    )


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_f')
    list_filter = ('id', 'nom_f')
    search_fields = ['nom_f']

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            # 'classes': ['collapse', ],
            'fields': ('nom_f', 'image', 'services')
        }),

    )


class Sous_CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_s_cat', 'categorie')
    list_filter = ('nom_s_cat', 'categorie')
    search_fields = ['nom_s_cat']
    fieldsets = (
        # Fieldset 1 : meta-info (nom)
        ('Général', {
            # 'classes': ['collapse', ],
            'fields': ('nom_s_cat', 'categorie')
        }),

    )


admin.site.register(Categorie)
admin.site.register(Sous_Categorie, Sous_CategorieAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
