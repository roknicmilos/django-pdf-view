from unittest.mock import patch

from django.http import FileResponse
from django.test import TestCase
from django.urls import reverse

from example.views import SinglePageExamplePDFView


class TestSinglePageExamplePDFView(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.render_css_patcher = patch(
            target='django_pdf_view.pdf.render_css',
            return_value=''
        )
        cls.render_css_patcher.start()

    def test_create_pdf(self):
        view = SinglePageExamplePDFView()
        pdf = view.create_pdf()

        self.assertEqual(pdf.get_title(), SinglePageExamplePDFView.title)
        self.assertEqual(pdf.get_filename(), SinglePageExamplePDFView.filename)
        self.assertEqual(
            pdf.template_name,
            SinglePageExamplePDFView.template_name
        )
        self.assertEqual(
            pdf._css_paths,
            [
                'django_pdf_view/css/pdf.css',
                *SinglePageExamplePDFView.css_paths,
            ]
        )

    def test_get_pdf(self):
        url_path = reverse('examples:single_page:pdf')
        response = self.client.get(path=url_path)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, FileResponse)

    def test_get_html(self):
        url_path = reverse('examples:single_page:html')
        response = self.client.get(path=url_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_download_pdf(self):
        url_path = reverse('examples:single_page:download')
        response = self.client.get(path=url_path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{SinglePageExamplePDFView.filename}"'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.render_css_patcher.stop()
