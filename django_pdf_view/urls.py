from django.urls import path, include

from django_pdf_view.views import (
    SinglePageExamplePDFView as SPView,
    MultiPageExamplePDFView as MPView,
)

app_name = 'django-pdf-view'

single_page_urlpatterns = [
    path('pdf/', SPView.as_view(response_type='pdf'), name='pdf'),
    path('html/', SPView.as_view(response_type='html'), name='html'),
    path(
        'download/',
        SPView.as_view(response_type='download'),
        name='download'
    ),
]

multi_page_urlpatterns = [
    path('pdf/', MPView.as_view(response_type='pdf'), name='pdf'),
    path('html/', MPView.as_view(response_type='html'), name='html'),
    path(
        'download/',
        MPView.as_view(response_type='download'),
        name='download'
    ),
]

urlpatterns = [
    path(
        'single-page/',
        include(
            (single_page_urlpatterns, 'django_pdf_view'),
            namespace='single_page'
        ),
    ),
    path(
        'multi-page',
        include(
            (multi_page_urlpatterns, 'django_pdf_view'),
            namespace='multi_page'
        ),
    ),
]
