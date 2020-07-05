from django.db import models
from django.utils import *
from blog.models import Categorie, Sous_Categorie, Service

class TypeElement(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    order = models.IntegerField()

    class Meta:
        verbose_name = "Type of Element"
        ordering = ["-order"]

    def __str__(self):
        return self.name

class Element(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title', null=True, blank=True)
    subTitle = models.CharField(max_length=255, verbose_name='Sub Title', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    image = models.ImageField(upload_to="../static", null=True, blank=True)
    color = models.CharField(max_length=10, verbose_name='Color', null=True, blank=True)
    minRowWidth = models.IntegerField(default=1, verbose_name='Minimum Width')
    url = models.URLField(max_length=200, null=True, blank=True)
    typeElemnt = models.ForeignKey(TypeElement, verbose_name='Type of Element', on_delete=models.CASCADE, default=1)
    order = models.IntegerField(default=0)

    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    sous_categorie = models.ForeignKey(Sous_Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)


    def hasResource(self):
        if self.categorie is None and self.sous_categorie is None and self.service is None:
            return False
        return True
    def getResource(self):
        if not self.categorie is None:
            return self.categorie
        if not self.sous_categorie is None:
            return self.categorie
        if not self.categorie is None:
            return self.service
        return None

    class Meta:
        verbose_name = "Element"
        ordering = ["-order"]

    def __str__(self):
        return self.title

class Tree(models.Model):
    in_home = models.BooleanField(default=False)
    name = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    element = models.ForeignKey(Element, verbose_name='Element', on_delete=models.SET_NULL, null=True,blank=True)
    root_node = models.ForeignKey('Node', verbose_name='Root',related_name='root', on_delete=models.SET_NULL, null=True,blank=True)
    color = models.CharField(max_length=10, verbose_name='Color', null=True, blank=True)
    rowWidth = models.IntegerField(default=1, verbose_name='Width')
    order = models.IntegerField()
    updated = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Tree"
        ordering = ["-order"]

    def toArray(self):
        return {
            'id': self.pk,
            'in_home': self.in_home,
            'name': self.name,
            'rowWidth': self.rowWidth,
            'updated': self.rowWidth,
        }

    def __str__(self):
        return self.name

class Node(models.Model):
    in_visible = models.BooleanField(default=True)
    description = models.TextField(max_length=30, verbose_name='Description', null=True, blank=True)
    father = models.ForeignKey('self', verbose_name='Tree', on_delete=models.CASCADE, null=True, blank=True)
    element_father = models.ForeignKey(Element, verbose_name='Element', related_name='tree_fathers', on_delete=models.CASCADE, null=True, blank=True)
    element = models.ForeignKey(Element, verbose_name='Element', related_name='tree_children', on_delete=models.CASCADE)
    color = models.CharField(max_length=10, verbose_name='Color', null=True)
    rowWidth = models.IntegerField(default=1, verbose_name='Width')
    order = models.IntegerField()
    is_root = models.BooleanField(default=False)
    tree = models.ForeignKey(Tree, verbose_name='Tree', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Node"
        ordering = ["-tree","-element_father","-order"]

    def __str__(self):
        return self.element + " " + self.typeElemnt + " (" + self.description + ") width:" + self.rowWidth
