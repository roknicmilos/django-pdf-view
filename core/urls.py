from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_pdf_view.urls', namespace='django_pdf_view')),
]
