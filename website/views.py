import tempfile
import uuid

from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

# Adapted from http://www.bedjango.com/blog/how-generate-pdf-django-weasyprint/
def generate_pdf(request):
    """Generate pdf."""
    # Model data
    items = [uuid.uuid4() for i in range(100)]

    # Rendered
    html_string = render_to_string('pdf.html', {'items': items})

    if 'html' in request.GET:
        return HttpResponse(html_string)

    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=items.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
