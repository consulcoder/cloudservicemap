from django import forms
from .models import *


"""class ServiceForm(forms.Form):
    class Meta:
        model = Service
        fields = '__all__' """


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['image', 'nom']
