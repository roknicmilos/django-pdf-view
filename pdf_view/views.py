from typing import Literal

from django.contrib import messages
from django.http import HttpResponse, FileResponse
from django.views import View

from pdf_view.decorators import with_tmp_env_var
from pdf_view.pdf import PDF


class PDFView(View):
    pdf_class: type[PDF] = PDF
    ResponseType = Literal['pdf', 'html', 'download']
    response_type: ResponseType | None = None
    title: str = None
    filename: str = None
    css_paths: list[str] = []
    template_name: str

    @classmethod
    def as_view(cls, response_type: ResponseType = None, **initkwargs):
        return super().as_view(response_type=response_type, **initkwargs)

    def __init__(self, *args, response_type: ResponseType = 'pdf', **kwargs):
        super().__init__(**kwargs)
        self.response_type = response_type

    def get(self, *args, **kwargs):
        if self.response_type == 'html':
            return self.html_response()

        if self.response_type == 'download':
            return self.download_pdf_response()

        return self.pdf_response()

    @with_tmp_env_var('QT_QPA_PLATFORM', 'offscreen')
    def pdf_response(self) -> FileResponse:
        """
        This response will display the PDF in the browser without
        downloading it.
        """
        pdf = self.create_pdf()
        return FileResponse(
            pdf.in_memory_pdf,
            filename=pdf.filename,
            content_type='application/pdf'
        )

    @with_tmp_env_var('QT_QPA_PLATFORM', 'offscreen')
    def download_pdf_response(self) -> FileResponse:
        """
        This response will download the PDF without displaying it
        in the browser.
        """
        pdf = self.create_pdf()
        response = FileResponse(
            pdf.in_memory_pdf,
            filename=pdf.filename,
            content_type='application/pdf'
        )
        content_disposition = f'attachment; filename="{pdf.filename}"'
        response['Content-Disposition'] = content_disposition
        return response

    def html_response(self) -> HttpResponse:
        """
        This response will display the HTML in the browser.
        """
        pdf = self.create_pdf()
        return HttpResponse(
            content=pdf.render_html(),
            content_type='text/html',
        )

    def create_pdf(self) -> PDF:
        kwargs = self.get_pdf_kwargs()
        return self.pdf_class(**kwargs)

    def get_pdf_kwargs(self) -> dict:
        return {
            'template_name': self.template_name,
            'title': self.title,
            'filename': self.filename,
            'context': self.get_context(),
            'css_paths': self.css_paths.copy(),
            'request': self.request,
        }

    def get_context(self) -> dict:
        context = {
            'response_type': self.response_type,
        }
        if self.response_type == 'html':
            # For some reason, regardless of how template is rendered,
            # messages collection is empty in the template, so we need
            # to pass it explicitly.
            context['messages'] = messages.get_messages(self.request)

        return context
