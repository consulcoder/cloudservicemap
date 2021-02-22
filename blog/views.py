from django.shortcuts import render
from blog.models import Service, Categorie, Fournisseur, Sous_Categorie
from tool.models import Tree
# libs para reporte pdf
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, mm
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate
from .filters import CategorieFilter, Sous_Categorie
from django.db.models import Q

this_path = os.getcwd() + '/blog/'
from django_xhtml2pdf.utils import generate_pdf


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


"""def pdf(request):
    # Create the HttpResponse headers with PDF
    response = HttpResponse(content_type='blog/pdf')
    response['Content-Disposition'] = 'atachement; filename=Cloud-Service-Map-student-report.pdf'
    # Create the PDF object, using the BytesIO object as its "file."
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 735, 'Report')
    c.setFont('Helvetica-Bold', 12)
    c.drawString(480, 750, "23/07/2020")
    c.drawImage('', 25, 480, 480, 270)
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response"""


def cloud(request):
    context = {}
    # context['fournisseur'] = Fournisseur.objects.all()
    # Requetes pour remplir les filtres
    context['fournisseurs'] = Fournisseur.objects.all()
    context['services'] = Service.objects.all()
    context['categories'] = Categorie.objects.all()
    context['souscategories'] = Sous_Categorie.objects.all()
    # Requetes filtrées
    four_form = request.GET.get('fournisseur')
    if four_form is None:
        context['fournisseur'] = Fournisseur.objects.all()
    else:
        context['fournisseur'] = Fournisseur.objects.filter(nom_f=request.GET['fournisseur'])

    cat_from_f = request.GET.get('categorie')
    if cat_from_f is None:
        context['categorie'] = Categorie.objects.all()
    else:

        GET = request.GET.copy()
        cat_from = GET.pop('categorie')
        for cat_from2 in cat_from:
            cat_from_f = cat_from2

        context['categorie'] = Categorie.objects.filter(nom_cat__in=cat_from)

    sous_categorie_form = request.GET.get('souscategorie')
    if sous_categorie_form is None:
        context['souscategorie'] = Sous_Categorie.objects.all()
    else:
        GET = request.GET.copy()
        sous_categorie_form1 = GET.pop('souscategorie')
        for sous_cat_item in sous_categorie_form1:
            sous_categorie_form = sous_categorie_form1
        context['souscategorie'] = Sous_Categorie.objects.filter(nom_s_cat__in=sous_categorie_form1)
    # context['souscategorie'] = Sous_Categorie.objects.all()
    context['Service'] = Service.objects.all()
    context['filtre'] = CategorieFilter(request.GET, queryset=Categorie.objects.all())
    return render(request, "blog/testhtml.html", context)


def filtre(request):
    filtre = CategorieFilter(request.GET, queryset=Categorie.objects.all())
    return render(request, 'blog/testhtml.html', {'filter': filtre})


def Categorie_list(request):
    f = CategorieFilter(request.GET, queryset=Categorie.objects.all())
    return render(request, 'my_app/template.html', {'filter': f})
