from django_pdf.pdf import PDF
from django_pdf.views.pdf_view import PDFView


class ExamplePDFView(PDFView):

    def create_pdf(self) -> PDF:
        pdf = PDF(
            template_name='django_pdf/example/pdf_example.html',
            title='Example PDF',
        )

        pdf.add_page(template_name='django_pdf/example/page_example.html')
        pdf.add_page(template_name='django_pdf/example/page_example.html')
        pdf.add_page(template_name='django_pdf/example/page_example.html')

        return pdf
