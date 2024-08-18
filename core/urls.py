from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'examples/',
        include('django_pdf_view.urls', namespace='examples')
    ),
]
