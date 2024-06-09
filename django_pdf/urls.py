from django.urls import path

from django_pdf.views import PDFView

app_name = 'django-pdf'

urlpatterns = [
    path('example/', PDFView.as_view(), name='example'),
]
