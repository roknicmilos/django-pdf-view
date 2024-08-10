from django.conf import settings

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
            context=self._get_first_page_context(),
        )

        return pdf

    def _get_first_page_context(self):
        address_url = (
            'https://www.google.rs/maps/place/Kornelija+Stankovi%C4%87a+39,'
            '+Novi+Sad/@45.2600114,19.8085096,15.91z/data=!4m6!3m5!1s0x475b'
            '11b16298fc2d:0xa5444cbbc3bf8f26!8m2!3d45.2605492!4d19.8103612!'
            '16s%2Fg%2F11fx0qw3pz?hl=hr&entry=ttu'
        )
        avatar_url = self.request.build_absolute_uri(
            f'{settings.STATIC_URL}cv/img/milos-roknic.png'
        )
        return {
            'avatar_url': avatar_url,
            'first_name': 'Miloš',
            'last_name': 'Roknić',
            'role': 'Software Engineer',
            'email': 'roknic.milos.994@gmail.com',
            'phone': '+385638455742',
            'address': {
                'label': 'Kornelija Stankovića 39, Novi Sad, 21000, Serbia',
                'url': address_url
            },
        }
