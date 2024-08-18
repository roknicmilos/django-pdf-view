from django_pdf_view.pdf import PDF
from django_pdf_view.services import create_pdf
from django_pdf_view.views.pdf_view import PDFView


class SinglePageExamplePDFView(PDFView):

    def create_pdf(self) -> PDF:
        return create_pdf(
            template_name='django_pdf_view/examples/single_page.html',
            title='Single Page Example PDF',
            filename='single_page_example_pdf.pdf',
        )


class MultiPageExamplePDFView(PDFView):

    def create_pdf(self) -> PDF:
        pdf = PDF(
            title='Multi Page Example PDF',
            filename='multi_page_example_pdf.pdf',
        )

        pdf.add_page(template_name='django_pdf_view/examples/multi_page_1.html')
        pdf.add_page(template_name='django_pdf_view/examples/multi_page_2.html')
        pdf.add_page(template_name='django_pdf_view/examples/multi_page_3.html')

        return pdf
