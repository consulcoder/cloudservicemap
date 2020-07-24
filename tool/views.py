import os, json
from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, inch
# import pyPdf
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from tool.models import *
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.template.loader import get_template
from xhtml2pdf import pisa
from Cloud_Service_Map import utils
from tool import utils as utils_tool

# this_path = os.getcwd() + '/tool/'
# Create your views here.
from django.views.generic import TemplateView, ListView

# Modelo Tree
def html_list_tree(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')

    items = Tree.objects.all()
    render(request, "tool/includes/list_tree.html", {'items': items})
def json_list_tree(request):
    # items = utils_tool.listCountRowOfCategory(Categorie.objects.get(pk=2))
    # print("------" + str(len(items)))
    return utils.jsonArray(Tree.objects.all())

def html_get_tree(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    pass
def pdf_get_tree(request):
    context = {}
    context['trees'] = []
    for tree in Tree.objects.filter(in_home=True).order_by('order'):
        context['trees'].append(tree.toArray())
        break
    return utils.print_pdf("pdf/index.html", context)

def json_get_tree(request):
# if not request.is_ajax():
#     return HttpResponseNotFound('<h1>Page not found</h1>')
    pk = request.GET['id']
    tree = Tree.objects.get(id=pk)
    fournisseur = Fournisseur.objects.all()
    arr_providers = utils.toArray(fournisseur)
    categories = Sous_Categorie.objects.filter(categorie_id=tree.categorie.id)
    arr_categories = []
    for categorie in categories:
        services = Service.objects.filter(sous_categorie_id=categorie.id)
        arr_categorie = categorie.toArray()
        arr_categorie['services'] = utils.toArray(services)
        arr_categories.append(arr_categorie)
    
    context = {
        'tree': tree.toArray(),
        'category': tree.categorie.toArray(),
        'categories': arr_categories,
        'fournisseur': arr_providers
    }
    return utils.json(context,200)
def json_get_struct(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')

def json_add_node(request):
    data = json.loads(request.body)
    # BUscando TypeElemnt
    id_typeElement = 1
    if data['resource_type']==2:
        id_typeElement = 2
    if data['resource_type']==3 or data['resource_type']==4:
        id_typeElement = 3
    typeElemnt = TypeElement.objects.get(pk=id_typeElement)
    # Creando instancia sin Recurso
    element = Element(color = data['color'], typeElemnt=typeElemnt)
    # Buscando Recurso
    image=None
    name=None
    url=None
    resource = None
    if data['resource_type']==2:
        resource = Sous_Categorie.objects.get(pk=data['resource_id'])
        name = resource.__str__()
        element.sous_categorie = resource
    if data['resource_type']==3:
        resource = Service.objects.get(pk=data['resource_id'])
        name = resource.__str__()
        image = resource.image
        url = resource.url
        element.service = resource
    if data['resource_type']==4:
        resource = Fournisseur.objects.get(pk=data['resource_id'])
        name = resource.__str__()
        image = resource.image
        # url = resource.url
        element.fournisseur = resource
    if data['resource_type']=='_':
        name = '_'
    #Guardando datos de Recursos
    element.title = name
    element.url = url
    element.image = image
    element.save()

    #Creando Nodo del Arbol
    tree = Tree.objects.get(pk=data['tree_id'])
    node_father = Node.objects.get(pk=data['father_id'])
    if id_typeElement == 3 and node_father.element.typeElemnt.id==2:
        node_father1 = Node.objects.create(
            color=tree.color,
            rowWidth=data['rowWidth'],
            father=node_father,
            tree=tree,
            element=Element.objects.create(color = 'transparent')
        )
        data['rowWidth'] = 12
        node_father = node_father1

    Node.objects.create(
        is_root=False,
        color=element.color,
        title=element.title,
        rowWidth=data['rowWidth'],
        father=node_father,
        tree=tree,
        element=element,
        url=url,
    )

    return utils.jsonArray(tree.getStruct(),200,'OK')
    
def json_edit_node(request):
    data = json.loads(request.body)
    node = Node.objects.get(pk=data['id'])
    node.rowWidth = data['rowWidth']
    node.title = data['title']
    node.color = data['color']
    node.url = data['url']
    node.save()
    return utils.json(node.toArray(),200,'OK')

def json_move_node(request):
    data = json.loads(request.body)
    node = Node.objects.get(pk=data['id'])
    direction = data['direction']
    width = node.rowWidth
    order = node.order

    # node.save()
    return utils.json(node.toArray(),200,direction)
    
def json_remove_node(request):
    data = json.loads(request.body)
    node = Node.objects.get(pk=data['id'])
    if node.father:
        for child in Node.objects.filter(father=node):
            if child.element.typeElemnt.id != 3:
                child.father = node.father
                child.save()
    node.delete()
    tree = Tree.objects.get(pk=data['tree_id'])
    return utils.jsonArray(tree.getStruct(),200,'OK')
def json_update_tree(request):
    data = json.loads(request.body)
    tree = Tree.objects.get(pk=data['id'])
    tree.linked = data['linked']
    tree.save()
    return utils.json(tree.toArray())
    
    pass
def json_remove_tree(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    pass