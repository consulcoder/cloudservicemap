from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.filter
@stringfilter
def two_points_trim(value):
    return value.strip('..').value.strip('/').strip('Cloud_Service_Map')