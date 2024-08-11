from abc import abstractmethod

from django.http import HttpResponse, FileResponse
from django.views import View

from django_pdf_view.decorators import with_tmp_env_var
from django_pdf_view.pdf import PDF


class PDFView(View):

    @with_tmp_env_var('QT_QPA_PLATFORM', 'offscreen')
    def get(self, *args, **kwargs):
        if self.request.GET.get('html') == 'true':
            return self.html_response()

        if self.request.GET.get('download') == 'true':
            return self.download_pdf_response()

        return self.pdf_response()

    def pdf_response(self) -> FileResponse:
        """
        This response will display the PDF in the
        browser without downloading it.
        """
        pdf = self.create_pdf()
        return FileResponse(pdf.in_memory_pdf, filename=pdf.filename)

    def download_pdf_response(self) -> FileResponse:
        """
        This response will download the PDF without
        displaying it in the browser.
        """
        pdf = self.create_pdf()
        response = FileResponse(pdf.in_memory_pdf, filename=pdf.filename)
        content_disposition = f'attachment; filename="{pdf.filename}"'
        response['Content-Disposition'] = content_disposition
        return response

    def html_response(self) -> HttpResponse:
        """
        This response will display the HTML in the
        browser.
        """
        pdf = self.create_pdf()
        return HttpResponse(
            content=pdf.render_html(),
            content_type='text/html',
        )

    @abstractmethod
    def create_pdf(self) -> PDF:
        pass  # pragma: no cover
