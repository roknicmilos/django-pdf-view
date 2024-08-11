from django.urls import path

from django_pdf_view import views

app_name = 'django-pdf-view'

urlpatterns = [
    path(
        'single-page-example/',
        views.SinglePageExamplePDFView.as_view(),
        name='single_page_example'
    ),
    path(
        'multi-page-example/',
        views.MultiPageExamplePDFView.as_view(),
        name='multi_page_example'
    ),
]
