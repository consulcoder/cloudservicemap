from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
RELATIVE_STATIC_URL = '../static/'


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.error():
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def json(data,code = 200,msg = ''):
    response = JsonResponse({'msg': msg, 'data': data})
    response.status_code = code
    return response
def toArray(data):
    items = []
    for item in data:
        items.append(item.toArray())
    return items
def jsonArray(data,code = 200,msg = ''):
    items = toArray(data)
    return json(items,code,msg)


