from django.urls import path

from .views import generate_pdf


app_name = 'website'


urlpatterns = [
    path('', generate_pdf, name='generate_pdf'),
]
