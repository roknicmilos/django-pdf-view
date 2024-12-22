from django.test import TestCase, RequestFactory

from pdf_view.views import PDFView


class ConcretePDFView(PDFView):
    template_name = 'pdf_view/pdf.html'
    filename = 'test.pdf'
    title = 'Test PDF'


class TestPDFView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.request_factory = RequestFactory()

    def test_create_pdf(self):
        view = ConcretePDFView()
        view.request = self.request_factory.get('/')
        pdf = view.create_pdf()
        self.assertEqual(pdf.template_name, ConcretePDFView.template_name)
        self.assertEqual(pdf.get_filename(), ConcretePDFView.filename)
        self.assertEqual(pdf.get_title(), ConcretePDFView.title)

    def test_html_response(self):
        view = ConcretePDFView()
        view.request = self.request_factory.get('/')
        response = view.html_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_pdf_response(self):
        view = ConcretePDFView()
        view.request = self.request_factory.get('/')
        response = view.pdf_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.filename}"'
        )

    def test_download_pdf_response(self):
        view = ConcretePDFView()
        view.request = self.request_factory.get('/')
        response = view.download_pdf_response()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.filename}"'
        )

    def test_get_method_with_html_response(self):
        request = self.request_factory.get('/')
        response = ConcretePDFView.as_view(response_type='html')(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_get_method_with_pdf_response(self):
        request = self.request_factory.get('/?html=true')
        response = ConcretePDFView.as_view(response_type='pdf')(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.filename}"'
        )

    def test_get_method_with_download_pdf_response(self):
        request = self.request_factory.get('/')
        response = ConcretePDFView.as_view(response_type='download')(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.filename}"'
        )
