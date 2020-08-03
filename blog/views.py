from django.shortcuts import render
from blog.models import Service, Categorie, Fournisseur, Sous_Categorie
from tool.models import Tree
# libs para reporte pdf
import os, json
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from .filters import CategorieFilter, Sous_Categorie
from django.db.models import Q

this_path = os.getcwd() + '/blog/'
# from django_xhtml2pdf.utils import generate_pdf


def index(request):
    context = {}
    context['servicecompute'] = Service.objects.filter(sous_categorie__categorie_id=2).filter(statut=True)
    context['servicestorage'] = Service.objects.filter(sous_categorie__categorie_id=1).filter(statut=True)
    context['fournisseur'] = Fournisseur.objects.all()
    context['categorie'] = Categorie.objects.all()
    context['souscategorie'] = Sous_Categorie.objects.all()
    context['services'] = Service.objects.filter(statut=True)
    context['trees'] = []
    for tree in Tree.objects.filter(in_home=True).order_by('order'):
        context['trees'].append(tree.toArray())
    return render(request, "blog/index.html", context)




def filtre(request):
    context = {}
    # context['fournisseur'] = Fournisseur.objects.all()
    # Requetes pour remplir les filtres
    context['fournisseurs'] = Fournisseur.objects.all()
    context['services'] = Service.objects.all()
    context['categories'] = Categorie.objects.all()
    context['souscategories'] = Sous_Categorie.objects.all()
    # Requetes filtrées
    providers_ids = request.GET.getlist('provider_ids')
    if len(providers_ids):
        context['fournisseur'] = Fournisseur.objects.filter(id__in=providers_ids)
    else:
        context['fournisseur'] = Fournisseur.objects.all()
    context['fournisseur_width'] = 4
    print(len(context['fournisseur']))
    if len(context['fournisseur']) == 1:
        context['fournisseur_width'] = 12
    if len(context['fournisseur']) == 2:
        context['fournisseur_width'] = 6
    if len(context['fournisseur']) == 4:
        context['fournisseur_width'] = 3

    category_ids = request.GET.getlist('category_ids')
    if len(category_ids):
        context['categorie'] = Categorie.objects.filter(id__in=category_ids)
    else:
        context['categorie'] = Categorie.objects.all()

    subcategory_ids = request.GET.getlist('subcategory_ids')
    if len(subcategory_ids):
        aux_sub = Sous_Categorie.objects.filter(id__in=subcategory_ids)
        aux_cat_ids = []
        category_ids = []
        for sub in aux_sub:
            if not aux_cat_ids.__contains__(sub.categorie.id):
                aux_cat_ids.append(sub.categorie.id)
        for cat in context['categorie']:
            if not aux_cat_ids.__contains__(cat.id):
                category_ids.append(cat.id)
        # print(aux_cat_ids)
        # print(category_ids)
        context['souscategorie'] = Sous_Categorie.objects.filter(Q(id__in=subcategory_ids) | Q(categorie__id__in=category_ids))
    else:
        context['souscategorie'] = Sous_Categorie.objects.all()
        
    # context['souscategorie'] = Sous_Categorie.objects.all()
    service_noms = request.GET.getlist('service_noms')
    if len(service_noms):
        context['Service'] = []
        aux_serv = {}
        for nom in service_noms:
            servs = Service.objects.filter(nom__contains=nom)
            for ser in servs:
                aux_serv[ser.id] = ser
        for key in iter(aux_serv):
            context['Service'].append(aux_serv[key])
    else:
        context['Service'] = Service.objects.all()
    context['filtre'] = CategorieFilter(request.GET, queryset=Categorie.objects.all())
    return render(request, "blog/filtering.html", context)


def cloud(request):
    context = {}
    context['fournisseurs'] = Fournisseur.objects.all()
    context['services'] = Service.objects.all()
    context['categories'] = Categorie.objects.all()
    context['souscategories'] = Sous_Categorie.objects.all()
    return render(request, 'blog/filters.html', context)


def Categorie_list(request):
    f = CategorieFilter(request.GET, queryset=Categorie.objects.all())
    return render(request, 'my_app/template.html', {'filter': f})

def json_list_subcategories(request):
    ids = request.GET.getlist('ids')
    response = HttpResponse()
    if not len(ids):
        ids = []
        for cat in Categorie.objects.all():
            ids.append(cat.id)
    for i in ids:
        category = Categorie.objects.get(id=i)
        response.write("<optgroup label='"+category.nom_cat+"'>")
        for sub in category.categories():
            response.write("<option value='"+str(sub.id)+"'>"+sub.nom_s_cat+"</option>")
        response.write("</optgroup>")
    return response

