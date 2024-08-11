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

    def test_create_pdf(self):
        view = ConcretePDFView()
        pdf = view.create_pdf()
        self.assertEqual(pdf, ConcretePDFView.sample_pdf)

    def test_html_response(self):
        view = ConcretePDFView()
        response = view.html_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_pdf_response(self):
        view = ConcretePDFView()
        response = view.pdf_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

    def test_download_pdf_response(self):
        view = ConcretePDFView()
        response = view.download_pdf_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

    def test_get_method_with_html_response(self):
        # When response type is not provided through view initialization,
        # it should be determined from the URL query parameters.
        request = self.request_factory.get('/?html=true')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

        # When response type is provided through view initialization,
        # it should override the URL query parameters.
        request = self.request_factory.get('/?download=true')
        response = ConcretePDFView.as_view(response_type='html')(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_get_method_with_pdf_response(self):
        # When response type is not provided through view initialization,
        # and it is not provided through URL query parameters,
        # it should default to 'pdf'.
        request = self.request_factory.get('/')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

        # When response type is provided through view initialization,
        # it should override the URL query parameters.
        request = self.request_factory.get('/?html=true')
        response = ConcretePDFView.as_view(response_type='pdf')(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

    def test_get_method_with_download_pdf_response(self):
        # When response type is not provided through view initialization,
        # it should be determined from the URL query parameters.
        request = self.request_factory.get('/?download=true')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

        # When response type is provided through view initialization,
        # it should override the URL query parameters.
        request = self.request_factory.get('/?html=true')
        response = ConcretePDFView.as_view(response_type='download')(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.sample_pdf.filename}"'
        )
