"""Cloud_Service_Map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog import views
import tool.views as tool_views
from rest_framework import routers
from django.urls import path, include



urlpatterns = [
    path('tool/tree/json_list', tool_views.json_list_tree),
    path('tool/tree/json_get/', tool_views.json_get_tree),
    path('grid/', views.service_grid),
    # Nous allons réécrire l'URL de l'accueil
    # path(r'^$', ListView.as_view(model=Service, context_object_name='Service', template_name='blog/index.html')),
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('', views.index),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    path('prueba/', views.my_main_view),
    path('prueba/second', views.my_second_views),
    path('testing/', views.testing),
    path('cloud/', views.cloud),

]

urlpatterns += staticfiles_urlpatterns()
