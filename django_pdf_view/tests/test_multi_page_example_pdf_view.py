from django.http import FileResponse
from django.test import TestCase
from django.urls import reverse

from django_pdf_view.views import MultiPageExamplePDFView


class TestMultiPageExamplePDFView(TestCase):

    def test_create_pdf(self):
        view = MultiPageExamplePDFView()
        pdf = view.create_pdf()

        self.assertEqual(pdf.get_title(), 'Multi Page Example PDF')
        self.assertEqual(pdf.get_filename(), 'multi_page_example_pdf.pdf')
        self.assertEqual(pdf.template_name, 'django_pdf_view/pdf.html')
        self.assertEqual(len(pdf.pages), 3)
        for page in pdf.pages:
            self.assertEqual(
                page.template_name,
                f'django_pdf_view/examples/multi_page_{page.number}.html'
            )

    def test_get_pdf(self):
        url_path = reverse('examples:multi_page:pdf')
        response = self.client.get(path=url_path)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, FileResponse)

    def test_get_html(self):
        url_path = reverse('examples:multi_page:html')
        response = self.client.get(path=url_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_download_pdf(self):
        url_path = reverse('examples:multi_page:download')
        response = self.client.get(path=url_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            'attachment; filename="multi_page_example_pdf.pdf"'
        )
