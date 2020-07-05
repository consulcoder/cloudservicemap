import os
from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, inch
# import pyPdf
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from blog.models import Service, Categorie
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.error():
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def json(data,code = 200,msg = ''):
    items = []
    for item in data:
        items.append(item.toArray())
    response = JsonResponse({'msg': msg, 'data': items})
    response.status_code = code
    return response

