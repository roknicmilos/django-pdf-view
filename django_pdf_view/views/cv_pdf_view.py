from django_pdf_view.pdf import PDF
from django_pdf_view.views import PDFView


class CVPDFView(PDFView):

    def create_pdf(self) -> PDF:
        pdf = PDF(
            title='CV | Miloš Roknić',
            filename='CV-Milos-Roknic-08-2024.pdf',
        )

        pdf.add_page(
            template_name='cv/cv.html',
            context={
                'base_url': self.request.build_absolute_uri('/'),
            }
        )

        return pdf
