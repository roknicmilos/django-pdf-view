from django.http import FileResponse
from django.test import TestCase

from django_pdf.views import ExamplePDFView


class TestExamplePDFView(TestCase):

    def test_create_pdf(self):
        view = ExamplePDFView()
        pdf = view.create_pdf()

        self.assertEqual(pdf.get_title(), 'Example PDF')
        self.assertEqual(pdf.get_filename(), 'pdf_example.pdf')
        self.assertEqual(
            pdf.template_name,
            'django_pdf/example/pdf_example.html'
        )
        self.assertEqual(len(pdf.pages), 3)
        for page in pdf.pages:
            self.assertEqual(
                page.template_name,
                'django_pdf/example/page_example.html'
            )

    def test_get_pdf(self):
        response = self.client.get('/pdf/example/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, FileResponse)

    def test_get_html(self):
        response = self.client.get('/pdf/example/?html=true')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_download_pdf(self):
        response = self.client.get('/pdf/example/?download=true')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            'attachment; filename="pdf_example.pdf"'
        )
