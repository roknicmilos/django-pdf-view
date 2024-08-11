from django.http import FileResponse
from django.test import TestCase
from django.urls import reverse_lazy

from django_pdf_view.views import SinglePageExamplePDFView


class TestSinglePageExamplePDFView(TestCase):
    url_path = reverse_lazy('django_pdf_view:single_page_example')

    def test_create_pdf(self):
        view = SinglePageExamplePDFView()
        pdf = view.create_pdf()

        self.assertEqual(pdf.get_title(), 'Single Page Example PDF')
        self.assertEqual(pdf.get_filename(), 'single_page_example_pdf.pdf')
        self.assertEqual(pdf.template_name, 'django_pdf_view/pdf.html')
        self.assertEqual(len(pdf.pages), 1)
        self.assertEqual(
            pdf.pages[0].template_name,
            'django_pdf_view/examples/single_page.html'
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
            'attachment; filename="single_page_example_pdf.pdf"'
        )
