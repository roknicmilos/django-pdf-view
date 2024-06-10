from django.urls import path

from django_pdf.views import ExamplePDFView

app_name = 'django-pdf'

urlpatterns = [
    path('example/', ExamplePDFView.as_view(), name='example'),
]
