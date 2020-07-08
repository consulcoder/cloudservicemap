from django.db import models
from django.utils import *
from blog.models import Categorie, Sous_Categorie, Service, Fournisseur
from Cloud_Service_Map import utils

class TypeElement(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    order = models.IntegerField(default=0)

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
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True, blank=True)


    def hasResource(self):
        if self.categorie is None and self.sous_categorie is None and self.service is None and self.fournisseur is None:
            return False
        return True
    def getResource(self):
        if not self.categorie is None:
            return self.categorie
        if not self.sous_categorie is None:
            return self.sous_categorie
        if not self.categorie is None:
            return self.service
        if not self.fournisseur is None:
            return self.fournisseur
        return None
    def getType(self):
        if not self.categorie is None:
            return 1
        if not self.sous_categorie is None:
            return 2
        if not self.categorie is None:
            return 3
        if not self.fournisseur is None:
            return 4
        return None

    def toArray(self):
        arr_r = None
        r = self.getResource()
        if r:
            arr_r = r.toArray()
        image_url = None
        if self.image:
            image_url = self.image.url
        return {
            'id': self.pk,
            'name': self.title,
            'title': self.title,
            'subTitle': self.subTitle,
            'image': image_url,
            'url': self.url,
            'color': self.color,
            'typeElement_id': self.typeElemnt.pk,
            'resource': arr_r,
            # 'resource_class': arr_r.__class__,
        }

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
    order = models.IntegerField(default=0)
    updated = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Tree"
        ordering = ["-order"]

    #BFS Iterator
    def getBFS(self):
        items = []
        stack = []
        stack.append(self.root_node)
        if self.root_node: 
            while(len(stack)):
                item = stack.pop()
                items.append(item)

                for node in Node.objects.filter(father=item, tree=self):
                    stack.insert(0,node)
        return items
    #DFS Iterator
    def getDFS(self,node,dfs_items):
        print(node)
        dfs_items.append(node)
        for child in Node.objects.filter(father=node, tree=self):
            #si es un contenedor funciona como hoja
            if node.element.typeElemnt.id == 1 and child.element.typeElemnt.id == 3: 
                # arr_child = child.toArray()
                # print(arr_child)
                # node.children.append({
                #     'id': child.pk
                # })
                i=0
            else:
                self.getDFS(child,dfs_items) #sino sigo con mi DFS

    def getStruct(self):
        dfs_items = []
        if not self.root_node is None:
            self.getDFS(self.root_node,dfs_items)
        return dfs_items
    def getStructBFS(self):
        return self.getBFS()
    
        


    def toArray(self):
        return {
            'id': self.pk,
            'in_home': self.in_home,
            'name': self.name,
            'color': self.color,
            'rowWidth': self.rowWidth,
            'updated': self.updated,
            'struct': utils.toArray(self.getStruct())
        }
    
    def save(self, *args, **kwargs):
        aux_id = self.id
        super().save(*args, **kwargs)  # Call the "real" save() method.
        if not aux_id:  # If it was new object
            element = Element.objects.create(
                title=self.name,
                color=self.color,
                categorie = self.categorie,
                typeElemnt = TypeElement.objects.get(pk=2)
            )
            node = Node.objects.create(
                is_root=True,
                color=self.color,
                title=self.name,
                tree=self,
                element=element,
                rowWidth=self.rowWidth
            )
            self.root_node = node
            self.element = element
            if self.id:
                self.save()

    def __str__(self):
        return self.name

class Node(models.Model):
    is_visible = models.BooleanField(default=True)
    title = models.CharField(max_length=30, verbose_name='Title', null=True, blank=True)
    subTitle = models.CharField(max_length=255, verbose_name='Sub Title', null=True, blank=True)
    description = models.TextField(max_length=30, verbose_name='Description', null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    father = models.ForeignKey('self', verbose_name='Father', on_delete=models.CASCADE, null=True, blank=True)
    element_father = models.ForeignKey(Element, verbose_name='Element', related_name='tree_fathers', on_delete=models.CASCADE, null=True, blank=True)
    element = models.ForeignKey(Element, verbose_name='Element', related_name='tree_children', on_delete=models.CASCADE)
    color = models.CharField(max_length=10, verbose_name='Color', null=True)
    rowWidth = models.IntegerField(default=1, verbose_name='Width')
    order = models.IntegerField(default=0)
    is_root = models.BooleanField(default=False)
    tree = models.ForeignKey(Tree, verbose_name='Tree', on_delete=models.CASCADE)

    def toArray(self):
        arr_element = self.element.toArray()
        father_id = None
        if self.father:
            father_id = self.father.pk
        children = []
        if self.element.typeElemnt.id == 1: 
            children = utils.toArray(Node.objects.filter(father=self, tree=self.tree, element__typeElemnt__id=3))
        return {
            'id': self.pk,
            'title': self.title,
            'subTitle': self.subTitle,
            'color': self.color,
            'rowWidth': self.rowWidth,
            'element': arr_element,
            'father_id': father_id,
            'tree_id': self.tree.pk,
            'is_root': self.is_root,
            'url': self.url,
            'children':children
        }
    class Meta:
        verbose_name = "Node"
        ordering = ["-tree","-element_father","-order"]

    def __str__(self):
        # return self.element.__str__() + " " + self.element.typeElemnt.__str__() + " (" + self.description + ") width:" + self.rowWidth
        return str(self.pk)
