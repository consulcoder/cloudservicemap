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
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView, ListView
# from blog.views import Fournisseur_List, categorie
from blog.models import Fournisseur, Service
from blog import views

# from blog.views import MainPageView

urlpatterns = [
    # Nous allons réécrire l'URL de l'accueil
    # path(r'^$', ListView.as_view(model=Service, context_object_name='Service', template_name='blog/index.html')),
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    # path('', views.inidex),
    # path('prueba/', views.service, name='service'),
    # path('prueba/', MainPageView.as_view(), name=''),
    path('prueba/', views.my_main_view),
    path('prueba/second', views.my_second_views),
    path('testing/', views.testing),
    path('new/', views.cloud),
    # path('test/', views.FAQView.as_view()),
    # path('fournisseur/', Fournisseur_List.as_view()),

]

urlpatterns += staticfiles_urlpatterns()
