from django.http import FileResponse
from django.test import TestCase
from django.urls import reverse_lazy

from django_pdf_view.views import MultipageExamplePDFView


class TestMultipageExamplePDFView(TestCase):
    url_path = reverse_lazy('pdf:multipage_example')

    def test_create_pdf(self):
        view = MultipageExamplePDFView()
        pdf = view.create_pdf()

        self.assertEqual(pdf.get_title(), 'Multipage Example PDF')
        self.assertEqual(pdf.get_filename(), 'multipage_example_pdf.pdf')
        self.assertEqual(pdf.template_name, 'django_pdf_view/pdf.html')
        self.assertEqual(len(pdf.pages), 3)
        for page in pdf.pages:
            self.assertEqual(
                page.template_name,
                f'django_pdf_view/examples/multipage_{page.number}.html'
            )

    def test_get_pdf(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, FileResponse)

    def test_get_html(self):
        response = self.client.get(f'{self.url_path}?html=true')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_download_pdf(self):
        response = self.client.get(f'{self.url_path}?download=true')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            'attachment; filename="multipage_example_pdf.pdf"'
        )
