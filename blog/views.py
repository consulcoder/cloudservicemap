from django.shortcuts import render
from blog.models import Service, Categorie, Fournisseur, Sous_Categorie
from tool.models import Tree
# libs para reporte pdf
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .filters import CategorieFilter
from django.views.generic import ListView, DetailView, TemplateView

this_path = os.getcwd() + '/blog/'
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CatList(ListView):
    queryset = Categorie.objects.all()
    context_object_name = 'cats'
    paginate_by = 0
    template_name = 'blog/pagination.html'


"""class CategorieListView(ListView):
    model = Categorie
    template_name = 'blog/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = ['filter'] = CategorieFilter(self.request.GET, queryset=self.get_queryset())
        return context"""


def index(request):
    context = {}
    context['servicecompute'] = Service.objects.filter(sous_categorie__categorie_id=2).filter(statut=True)
    context['servicestorage'] = Service.objects.filter(sous_categorie__categorie_id=1).filter(statut=True)
    context['fournisseur'] = Fournisseur.objects.all()
    context['gjhh'] = Categorie.objects.filter(nom_cat="Compute")
    context['categorie'] = Categorie.objects.all()
    context['souscategorie'] = Sous_Categorie.objects.all()
    context['services'] = Service.objects.filter(statut=True)
    context['trees'] = []
    for tree in Tree.objects.filter(in_home=True).order_by('order'):
        context['trees'].append(tree.toArray())
    return render(request, "blog/index.html", context)


def cloud(request):
    context = {}
    context['fournisseur'] = Fournisseur.objects.all()
    cat_from = request.GET.get('categorie')
    if cat_from is None:
        context['categorie'] = Categorie.objects.all()
    else:
        context['categorie'] = Categorie.objects.filter(nom_cat=request.GET['categorie'])

    context['souscategorie'] = Sous_Categorie.objects.all()
    context['Service'] = Service.objects.all()
    context['filtre'] = CategorieFilter(request.GET, queryset=Categorie.objects.all())
    return render(request, "blog/testhtml.html", context)


"""def pagination(request):
    cat_list = Categorie.objects.all()
    paginator = Paginator(cat_list, 3)
    page = request.GET.get('page')
    try:
        cats = paginator.page(page)
    except PageNotAnInteger:
        cats = paginator.page(1)
    except EmptyPage:
        cats = paginator.page(paginator.num_pages)
    # ?page=2
    
    return render(request, "blog/pagination.html", {'page': page, 'cats': cats, })


def filtre(request):
    filtre = CategorieFilter(request.GET, queryset=Categorie.objects.all())
    return render(request, 'blog/search.html', {'filter': filtre})"""

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
