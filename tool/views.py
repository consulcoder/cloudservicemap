import os, json
from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, inch
# import pyPdf
from shutil import make_archive
from wsgiref.util import FileWrapper
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from tool.models import *
from django.db.models import Q, Max
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.template.loader import get_template
from xhtml2pdf import pisa
from Cloud_Service_Map import utils
from tool import utils as utils_tool
import shutil
# this_path = os.getcwd() + '/tool/'
# Create your views here.
from django.views.generic import TemplateView, ListView
from blog.models import Categorie, Sous_Categorie, Service, Fournisseur


# import excel as excel
# Descarga de Csv

# def dowlandcvs(request):
#     export=[]
#     export.append(['Categorie','Sous_Categorie','Service','Fournisseur'])
#     resultado=Service.ob
#     for result in resultado:
#         export.append([ser])


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
    return utils.json(context, 200)


def json_get_struct(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')


def json_add_node(request):
    data = json.loads(request.body)
    # BUscando TypeElemnt
    id_typeElement = 1
    if data['resource_type'] == 2:
        id_typeElement = 2
    if data['resource_type'] == 3 or data['resource_type'] == 4:
        id_typeElement = 3
    typeElemnt = TypeElement.objects.get(pk=id_typeElement)
    # Creando instancia sin Recurso
    element = Element(color=data['color'], typeElemnt=typeElemnt)
    # Buscando Recurso
    image = None
    name = None
    url = None
    resource = None
    if data['resource_type'] == 2:
        resource = Sous_Categorie.objects.get(pk=data['resource_id'])
        name = resource.__str__()
        element.sous_categorie = resource
    if data['resource_type'] == 3:
        resource = Service.objects.get(pk=data['resource_id'])
        name = resource.__str__()
        image = resource.image
        url = resource.url
        element.service = resource
    if data['resource_type'] == 4:
        resource = Fournisseur.objects.get(pk=data['resource_id'])
        name = resource.__str__()
        image = resource.image
        # url = resource.url
        element.fournisseur = resource
    if data['resource_type'] == '_':
        name = '_'
    # Guardando datos de Recursos
    element.title = name
    element.url = url
    element.image = image
    element.save()

    # Creando Nodo del Arbol
    tree = Tree.objects.get(pk=data['tree_id'])
    order = 0
    node_father = Node.objects.get(pk=data['father_id'])
    if id_typeElement == 3 and node_father.element.typeElemnt.id == 2:
        node_father1 = Node.objects.create(
            color=tree.color,
            rowWidth=data['rowWidth'],
            father=node_father,
            tree=tree,
            element=Element.objects.create(color='transparent')
        )
        data['rowWidth'] = 12
        node_father = node_father1

    # Calculo del Orden
    o = (Node.objects.filter(father=node_father).aggregate(Max('order')))
    print(o)
    order = o.get('order__max')
    if order:
        order = order + 1
    else:
        order = 0

    Node.objects.create(
        is_root=False,
        color=element.color,
        title=element.title,
        rowWidth=data['rowWidth'],
        father=node_father,
        tree=tree,
        element=element,
        url=url,
        order=order
    )

    return utils.jsonArray(tree.getStruct(), 200, 'OK')


def json_edit_node(request):
    data = json.loads(request.body)
    node = Node.objects.get(pk=data['id'])
    node.rowWidth = data['rowWidth']
    node.title = data['title']
    node.color = data['color']
    node.url = data['url']
    node.save()
    return utils.json(node.toArray(), 200, 'OK')


def json_move_node(request):
    data = json.loads(request.body)
    direction = data['direction']
    node = Node.objects.get(pk=data['id'])
    # Arrglando orden de nodos hijos
    i = 0
    for child in Node.objects.filter(father=node.father).order_by('order'):
        i = i + 1
        print("¡¡¡¡¡¡¡¡¡")
        print(child)
        print(str(child.order) + ' ' + str(i))
        print("¡¡¡¡¡¡¡¡¡")
        child.order = i
        child.save()
    # Moviendo segun la direccion
    node = Node.objects.get(pk=data['id'])
    if direction == 'prev' and i > 1:
        try:
            prev_node = Node.objects.get(father=node.father, order=node.order - 1)
            prev_node.order += 1
            prev_node.save()
            node.order -= 1
            node.save()
        except Node.DoesNotExist:
            pass

    if direction == 'next':
        try:
            next_node = Node.objects.get(father=node.father, order=node.order + 1)
            next_node.order -= 1
            next_node.save()
        except Node.DoesNotExist:
            element = Element(title='_', typeElemnt=TypeElement.objects.get(pk=1))
            element.save()
            Node.objects.create(
                is_root=False,
                title='_',
                rowWidth=node.rowWidth,
                father=node.father,
                tree=node.tree,
                element=element,
                order=node.order
            )
        node.order += 1
        node.save()

    # node.save()
    return utils.jsonArray(node.tree.getStruct(), 200, direction)


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
    return utils.jsonArray(tree.getStruct(), 200, 'OK')


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


from shutil import rmtree
from datetime import datetime
from blog.views import getFiltre


def download(request, file_name="Nuegeo_packet"):
    # a = len(str(request.GET))
    # providers_ids = request.GET.getlist('provider_ids')
    # print(len(providers_ids))

    # print(request.GET.getlist('category_ids[]'))
    
    # for key in iter(request.GET):
        
    #     print(key)
    #     print(request.GET[key])

    # if a > 15:  # EL REQUEST VACIO TIENE UN LARGO ESTANDAR DE 15
    #     pa = []
    #     a = request.GET.getlist('category_ids[0]')
    #     c = Categorie.objects.filter(id__in=a)
    #     pa.append(c)
    #     a = request.GET.getlist('subcategory_ids[0]')
    #     c = Sous_Categorie.objects.filter(id__in=a)
    #     pa.append(c)
    #     a = request.GET.getlist('service_noms[0]')
    #     pa.append(a)
    #     a = request.GET.getlist('provider_ids[0]')
    #     c = Fournisseur.objects.filter(id__in=a)
    #     pa.append(c)
    #     # print(pa)

    #     # creando carpeta temporal
    #     files_path = 'static' + os.path.sep + 'temp_zip'
    #     os.mkdir(files_path)
    #     # crando fichero csv
    #     fich = open(files_path + os.path.sep + 'data.csv', 'w')
    #     ##creando linea de columna
    #     line = 'Categorie,Souscategorie,Service,Fournisseur\n'
    #     fich.writelines(line)
    #     data_pa = str(pa)
    #     fich.writelines(data_pa)

    #     fich.close()
    #     # creando fichero comprimido
    #     relative_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.path.sep + files_path
    #     path_to_zip = make_archive(files_path, "gztar", relative_path)
    #     fich = open(path_to_zip, 'rb')
    #     response = HttpResponse(FileWrapper(fich), content_type='application/zip')
    #     response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
    #         filename=file_name.replace(" ", "_")
    #     )
    #     # eliminado carpeta temporal
    #     rmtree(files_path)
    #     return response


    # else:

        # creando carpeta temporal
        files_path = 'static' + os.path.sep + 'temp_zip'
        os.mkdir(files_path)
        # crando fichero csv
        fich = open(files_path + os.path.sep + 'data.csv', 'w')
        ##creando linea de columna
        line = 'Categorie,Souscategorie,Service,Fournisseur\n'
        fich.writelines(line)
        # obtniendo datos
        subcategory_ids_1 = request.GET.getlist('subcategory_ids')
        # print(request.GET)
        print(subcategory_ids_1)
        print(len(subcategory_ids_1))
        data = getFiltre(request)
        for serv in data['services']:
            # añadiendo liniea de la BD
            line = serv.sous_categorie.categorie.nom_cat + ',' + serv.sous_categorie.nom_s_cat + ',' + serv.nom + ',' + serv.fournisseurs + '\n'
            fich.writelines(line)
        fich.close()
        # creando fichero comprimido
        relative_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.path.sep + files_path
        path_to_zip = make_archive(files_path, "gztar", relative_path)
        fich = open(path_to_zip, 'rb')
        response = HttpResponse(FileWrapper(fich), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
            filename=file_name.replace(" ", "_")
        )
        # eliminado carpeta temporal
        rmtree(files_path)
        return response


def carga(request):
    print('aqui')
    import zipfile
    ruta_zip = "pack/hola.zip"
    ruta_extraccion = "static/upload_pack"
    password = None
    archivo_zip = zipfile.ZipFile(ruta_zip, "r")
    try:
        print(archivo_zip.namelist())
        archivo_zip.extractall(pwd=password, path=ruta_extraccion)
    except:
        pass
    archivo_zip.close()
    #rmtree("static/upload_pack")











# ESTE SIIIII

# from django.shortcuts import render
# from django.views.generic.edit import FormView
#
# from .forms import FormUpload
#
#
# class UploadFileView(FormView):
#     '''
#     Esta vista sube un archivo al servidor
#     '''
#     template_name = "filters.html"
#     form_class = FormUpload
#     success_url = '/'
#
#     def get(self, request, *args, **kwargs):
#
#         data = {'form': self.form_class}
#
#         return render(request, self.template_name, data)
#
#     def post(self, request, *args, **kwargs):
#
#         form = FormUpload(request.POST, request.FILES)
#         if form.is_valid():
#             if 'UP' in request.FILES:
#                 UP = request.FILES['UP']
#                 form.handle_uploaded_file(UP)
#                 return self.form_valid(form, **kwargs)
#
#             else:
#                 return self.form_invalid(form, **kwargs)
#         else:
#             return self.form_invalid(form, **kwargs)