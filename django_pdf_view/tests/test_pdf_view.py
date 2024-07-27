import os

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

    def test_view_setup(self):
        """
        Test that the view `setup` method sets the QT_QPA_PLATFORM
        environment variable to 'offscreen'.

        Setting QT_QPA_PLATFORM environment variable to 'offscreen'
        is necessary for wkhtmltopdf to work properly in some
        environments because it ensures that the Qt framework operates
        in offscreen mode.

        wkhtmltopdf relies on Qt for rendering HTML to PDF.
        Without a display server, rendering won't work unless Qt is
        instructed to use an offscreen mode.
        """
        factory = RequestFactory()
        request = factory.get('/')
        view = ConcretePDFView()
        os.environ['QT_QPA_PLATFORM'] = 'not_offscreen'
        view.setup(request)
        self.assertEqual(os.environ['QT_QPA_PLATFORM'], 'offscreen')

    def test_create_pdf(self):
        view = ConcretePDFView()
        pdf = view.create_pdf()
        self.assertEqual(pdf, ConcretePDFView.sample_pdf)

    def test_html_response(self):
        factory = RequestFactory()
        request = factory.get('/?html=true')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html')

    def test_file_response(self):
        factory = RequestFactory()
        request = factory.get('/')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'inline; filename="{ConcretePDFView.sample_pdf.filename}"'
        )

    def test_download_response(self):
        factory = RequestFactory()
        request = factory.get('/?download=true')
        response = ConcretePDFView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(
            response['Content-Disposition'],
            f'attachment; filename="{ConcretePDFView.sample_pdf.filename}"'
        )
