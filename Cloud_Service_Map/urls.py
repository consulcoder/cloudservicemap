"""Cloud_Service_Map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')cloudservicemap
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from myapp import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog import views
from blog.views import *
import tool.views as tool_views
from myapp import views as upload
# from blog.views import MainPageView

urlpatterns = [
    path('tool/tree/json_list', tool_views.json_list_tree),
    path('tool/tree/json_get/', tool_views.json_get_tree),
    path('tool/tree/json_get_struct/', tool_views.json_get_struct),
    path('admin/tool/tree/json_update/', tool_views.json_update_tree),
    path('admin/tool/tree/json_add_node/', tool_views.json_add_node),
    path('admin/tool/tree/json_edit_node/', tool_views.json_edit_node),
    path('admin/tool/tree/json_move_node/', tool_views.json_move_node),
    path('admin/tool/tree/json_remove_node/', tool_views.json_remove_node),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    path('', views.index),
    path('CSM/', views.cloud),
    path('CSM/filters', views.filtre),
    path('CSM/json_list_subcategories', views.json_list_subcategories),
    path('CSV/download',  tool_views.download),#Link de descarga de Csv
    path('CSV/export',tool_views.carga),
    path('CSV/import',upload.my_view,name='my-view')


]

urlpatterns += staticfiles_urlpatterns()
