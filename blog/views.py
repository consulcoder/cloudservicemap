from django.shortcuts import render
from blog.models import Service, Categorie, Fournisseur, Sous_Categorie
from tool.models import Tree


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
