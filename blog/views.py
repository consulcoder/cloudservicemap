from django.shortcuts import render
from blog.models import Service, Categorie, Fournisseur, Sous_Categorie
from tool.models import Tree
# libs para reporte pdf
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate

this_path = os.getcwd() + '/blog/'
from django_xhtml2pdf.utils import generate_pdf


def myview(request):
    resp = HttpResponse(content_type='application/pdf')
    dynamic_variable = request.user.some_special_something
    context = {'some_context_variable': dynamic_variable}
    result = generate_pdf('my_template.html', file_object=resp, context=context)
    return result


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
    return render(request, "blog/pdf.html")"""


def pdf(request):
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

    return response


"""def testinpdf(request):
    pdf_buffer = BytesIO()
    my_doc = SimpleDocTemplate(pdf_buffer)
    box = {
        'nom': 'for nom_four'
               ''
    }"""
