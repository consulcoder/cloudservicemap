from django.contrib import admin
from blog.models import Categorie, Sous_Categorie, Service, Fournisseur


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'sous_categorie', 'image', 'statut', 'fournisseurs', 'url')
    list_filter = ('nom', 'categorie', 'sous_categorie')
    search_fields = ('nom', 'categorie', 'sous_categorie')

    fieldsets = (
        # Fieldset 1 : meta-info (nom)
        ('Général', {
            # 'classes': ['collapse', ],
            'fields': ('nom', 'categorie', 'sous_categorie', 'image', 'statut', 'fournisseurs', 'url')
        }),

    )


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom_f', 'image')
    list_filter = ('nom_f', 'image', 'services')
    search_fields = ('nom', 'services', 'services')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            # 'classes': ['collapse', ],
            'fields': ('nom_f', 'image', 'services')
        }),

    )

class Sous_CategorieAdmin(admin.ModelAdmin):

        list_display = ('nom_s_cat', 'categorie')
        list_filter = ('nom_s_cat',)
        search_fields = ('nom_s_cat',)

        fieldsets = (
            # Fieldset 1 : meta-info (nom)
            ('Général', {
                # 'classes': ['collapse', ],
                'fields': ('nom_s_cat', )
            }),

        )


admin.site.register(Categorie)
admin.site.register(Sous_Categorie, Sous_CategorieAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
