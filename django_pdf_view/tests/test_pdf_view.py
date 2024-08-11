from django.test import TestCase, RequestFactory

from django_pdf_view.pdf import PDF
from django_pdf_view.views import PDFView


class ConcretePDFView(PDFView):
    sample_pdf = PDF(
        template_name='django_pdf_view/pdf.html',
        language='en',
        filename='test.pdf',
        title='Test PDF'
    )

    def create_pdf(self):
        return self.sample_pdf


class TestPDFView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.request_factory = RequestFactory()
        cls.view = ConcretePDFView()

    def test_create_pdf(self):
        pdf = self.view.create_pdf()
        self.assertEqual(pdf, ConcretePDFView.sample_pdf)

    def test_html_response(self):
        response = self.view.html_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_pdf_response(self):
        response = self.view.pdf_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

    def test_download_pdf_response(self):
        response = self.view.download_pdf_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

    def test_get_method_with_html_response(self):
        request = self.request_factory.get('/?html=true')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_get_method_with_pdf_response(self):
        request = self.request_factory.get('/')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

    def test_get_method_with_download_pdf_response(self):
        request = self.request_factory.get('/?download=true')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.sample_pdf.filename}"'
        )
