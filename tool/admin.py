from django.contrib import admin
from tool.models import TypeElement, Element, Node, Tree
from blog.models import *


# Register your models here.


class TypeElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'order')
    list_filter = ('name', 'description', 'order')
    search_fields = ('name', 'description', 'order')

    fieldsets = (
        # Fieldset 1 : meta-info (nom)
        ('Général', {
            # 'classes': ['collapse', ],
            'fields': ('name', 'description')
        }),

    )


class TreeAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'in_home', 'description', 'color', 'rowWidth', 'order', 'linked')
    list_filter = ('name', 'order')
    search_fields = ('name', 'order')
    exclude = ('updated', 'element', 'root_node', 'max_category_column')


# Register your models here.

admin.site.register(Tree, TreeAdmin)
