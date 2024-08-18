from abc import abstractmethod
from typing import Literal

from django.http import HttpResponse, FileResponse
from django.views import View

from django_pdf_view.decorators import with_tmp_env_var
from django_pdf_view.pdf import PDF


class PDFView(View):
    ResponseType = Literal['pdf', 'html', 'download']
    response_type: ResponseType | None = None

    @classmethod
    def as_view(cls, response_type: ResponseType = None, **initkwargs):
        return super().as_view(response_type=response_type, **initkwargs)

    def __init__(self, *args, response_type: ResponseType = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.response_type = response_type

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        if self.response_type:
            pass
        elif self.request.GET.get('html') == 'true':
            self.response_type = 'html'
        elif self.request.GET.get('download') == 'true':
            self.response_type = 'download'
        else:
            self.response_type = 'pdf'

    def get(self, *args, **kwargs):
        if self.response_type == 'html':
            return self.html_response()

        if self.response_type == 'download':
            return self.download_pdf_response()

        return self.pdf_response()

    @with_tmp_env_var('QT_QPA_PLATFORM', 'offscreen')
    def pdf_response(self) -> FileResponse:
        """
        This response will display the PDF in the
        browser without downloading it.
        """
        pdf = self.create_pdf()
        return FileResponse(pdf.in_memory_pdf, filename=pdf.filename)

    @with_tmp_env_var('QT_QPA_PLATFORM', 'offscreen')
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
