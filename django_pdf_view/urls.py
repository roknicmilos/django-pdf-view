from django.urls import path

from django_pdf_view import views

app_name = 'django-pdf-view'

urlpatterns = [
    path(
        'singlepage-example/',
        views.SinglepageExamplePDFView.as_view(),
        name='singlepage_example'
    ),
    path(
        'multipage-example/',
        views.MultipageExamplePDFView.as_view(),
        name='multipage_example'
    ),
]
