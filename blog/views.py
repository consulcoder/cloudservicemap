import os
from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, inch
# import pyPdf
from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Service, Categorie, Fournisseur
from django.template.loader import get_template
from xhtml2pdf import pisa
# this_path = os.getcwd() + '/blog/'
# Create your views here.
from django.views.generic import TemplateView, ListView
from blog.models import Service, Fournisseur


def fournisseur(request):
    cont = Fournisseur.objects.all()
    print(cont)
    return render(request, "blog/prueba.html", {'fournisseur': cont})


def my_main_view(request):
    context = {}
    context['fournisseur'] = Fournisseur.objects.all()
    context['service'] = Service.objects.all()
    return render(request, 'blog/prueba.html', context)


def my_second_views(request):
    return render(request, "blog/prueba1.html")


def inidex(request):
    return render(request, "blog/inidex.html")


def testing(request):
    context = Service.objects.all()
    print(context)
    return render(request, "blog/prueba1.html", {'context': context})


def cloud(request):
    context = {}
    context['service'] = Service.objects.filter
    return render(request, "blog/new.html", context)


"""def prueba(request):
    service = Fournisseur.objects.all()
    return render(request, "blog/prueba.html", {'service': service})"""

"""def service(request):
    images = Service.objects.all()
    print(images)
    return render(request, 'blog/index.html', {'images': images})"""


def voir_Fournisseur(request):
    return render(
        request,
        'blog/index.html',
        {'fournisseur': Fournisseur.objects.all()}
    )


"""def pedido(request):
    nom_f = Fournisseur(int([0]), int([1]), int([2]))
    pedidos = models.Pedido.objects.filter(fecha_despacho=fecha)
    resultado = []
    for i in pedidos:
        detalles = models.Detalle.objects.filter(pedido=i.id)
        productos = []
        for j in detalles:


productos.append([j.producto.nombre, j.cantidad_detalle, j.valor_detalle])
resultado.append([i.cliente.nombre, 1, i.valor_total, productos])
return render_to_response('templates/ListarPedido.html', {
    'opcion': fecha,
    'resultado': resultado})"""
"""class Fournisseur_List(ListView):
    context_object_name = "mes_fournisseur"
    queryset = Fournisseur.objects.all()
    #template_name = 'blog/test.html'
    render(ListView, 'blog/test.html', queryset)"""

"""pour afficher mes fournisseur côyé template
def fournisseur(request):
    fournisseur = Fournisseur.objects.all()
    print(fournisseur)
    return render(request, 'blog/index.html', {'fournisseur': fournisseur})"""

"""def fournisseur(request):
    images = Fournisseur.objects.all()
    print(images)
    return render(request, 'blog/list.html', {'images': images})"""

"""def categorie(request):
    cat = Categorie.objects.all()
    cont = {'categorie': cat}
    return render(request, 'blog/index.html', cont)"""

"""def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.error():
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None"""

"""def report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Diposition'] = 'attachement; filename = Cloud_Service_Map.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)
    c.drawString(30, 750, 'Cloud_Service_Map.pdf')
    c.setFont('Helvetica', 12)
    c.drawString(480, 750, "11/06/2020")
    c.line(460, 747, 560, 747)
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response"""
