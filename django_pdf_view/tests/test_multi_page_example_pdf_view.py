from django.http import FileResponse
from django.test import TestCase
from django.urls import reverse

from django_pdf_view.views.examples import MultiPageExamplePDFView


class TestMultiPageExamplePDFView(TestCase):

    def test_create_pdf(self):
        view = MultiPageExamplePDFView()
        pdf = view.create_pdf()

        self.assertEqual(pdf.get_title(), MultiPageExamplePDFView.title)
        self.assertEqual(pdf.get_filename(), MultiPageExamplePDFView.filename)
        self.assertEqual(
            pdf.template_name,
            MultiPageExamplePDFView.template_name
        )
        self.assertEqual(
            pdf._css_paths,
            [
                'django_pdf_view/css/pdf.css',
                *MultiPageExamplePDFView.css_paths,
            ]
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
            f'attachment; filename="{MultiPageExamplePDFView.filename}"'
        )
