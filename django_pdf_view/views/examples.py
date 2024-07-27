from django_pdf_view.pdf import PDF
from django_pdf_view.services import create_pdf
from django_pdf_view.views.pdf_view import PDFView


class SinglepageExamplePDFView(PDFView):

    def create_pdf(self) -> PDF:
        return create_pdf(
            template_name='django_pdf_view/examples/singlepage.html',
            title='Singlepage Example PDF',
            filename='singlepage_example_pdf.pdf',
        )


class MultipageExamplePDFView(PDFView):

    def create_pdf(self) -> PDF:
        pdf = PDF(
            title='Multipage Example PDF',
            filename='multipage_example_pdf.pdf',
        )

        pdf.add_page(template_name='django_pdf_view/examples/multipage_1.html')
        pdf.add_page(template_name='django_pdf_view/examples/multipage_2.html')
        pdf.add_page(template_name='django_pdf_view/examples/multipage_3.html')

        return pdf
