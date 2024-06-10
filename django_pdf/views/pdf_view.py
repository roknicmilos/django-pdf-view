import os
from abc import abstractmethod

from django.http import HttpResponse, FileResponse
from django.views import View

from django_pdf.pdf import PDF


class PDFView(View):

    def get(self, *args, **kwargs):
        os.environ['QT_QPA_PLATFORM'] = 'offscreen'

        pdf = self.create_pdf()

        if self.request.GET.get('html') == 'true':
            return HttpResponse(
                content=pdf.render_html(),
                content_type='text/html',
            )

        response = FileResponse(pdf.in_memory_pdf, filename=pdf.filename)

        if self.request.GET.get('download') == 'true':
            content_disposition = f'attachment; filename="{pdf.filename}"'
            response['Content-Disposition'] = content_disposition

        return response

    @abstractmethod
    def create_pdf(self) -> PDF:
        pass
