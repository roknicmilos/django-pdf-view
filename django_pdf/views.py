from django.http import HttpResponse, FileResponse
from django.views import View

from django_pdf.pdf import PDF


class PDFView(View):
    def get(self, *args, **kwargs):
        pdf = self._create_pdf()

        if self.request.GET.get('html') == 'true':
            return HttpResponse(
                content=pdf.render_html(),
                content_type='text/html',
            )

        # TODO: FIX THIS!
        response = FileResponse(pdf.in_memory_pdf, filename=pdf.filename)
        content_disposition = f'attachment; filename="{pdf.filename}"'
        response['Content-Disposition'] = content_disposition
        return response

    @staticmethod
    def _create_pdf() -> PDF:
        pdf = PDF(
            template_name='example/pdf_example.html',
            title='Example PDF',
        )

        pdf.add_page(template_name='example/page_example.html')
        pdf.add_page(template_name='example/page_example.html')
        pdf.add_page(template_name='example/page_example.html')

        return pdf
