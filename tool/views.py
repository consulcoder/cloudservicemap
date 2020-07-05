import os
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
    return utils.json(Tree.objects.all())

def html_get_tree(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    pass
def pdf_get_tree(request):
    pass
def json_get_tree(request):
# if not request.is_ajax():
#     return HttpResponseNotFound('<h1>Page not found</h1>')
    pk = request.GET['id']
    # item = Tree.objects.get(pk)
    # categories = item.categorie.
    
    return utils.json([],200,request.GET['id'])
def json_update_tree(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    pass
def json_remove_tree(request):
    if not request.is_ajax():
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    pass