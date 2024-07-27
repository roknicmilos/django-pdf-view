from unittest import TestCase
from unittest.mock import patch
from io import BytesIO

from django_pdf_view.pdf import PDF
from django_pdf_view.pdf_page import PDFPage


class TestPDF(TestCase):

    def setUp(self):
        super().setUp()
        self.render_page_html_patcher = patch(
            target='django_pdf_view.pdf_page.PDFPage.render_html',
            return_value='<div>PDF Page</div>'
        )
        self.mock_render_page_html = self.render_page_html_patcher.start()

    def test_initialization(self):
        pdf = PDF(
            template_name='pdf.html',
            language='en',
            filename='test.pdf',
            title='Test PDF'
        )
        self.assertEqual(pdf.template_name, 'pdf.html')
        self.assertEqual(pdf.language, 'en')
        self.assertEqual(pdf.filename, 'test.pdf')
        self.assertEqual(pdf._title, 'Test PDF')
        self.assertEqual(pdf.pages, [])

    def test_add_page(self):
        pdf = PDF(template_name='pdf.html')
        pdf.add_page(template_name='pdf_page.html')
        self.assertEqual(len(pdf.pages), 1)
        self.assertIsInstance(pdf.pages[0], PDFPage)
        self.assertEqual(pdf.pages[0].template_name, 'pdf_page.html')

    @patch('django_pdf_view.pdf.render_to_string')
    def test_render_html(self, mock_render_pdf_to_string):
        mock_render_pdf_to_string.return_value = '<html>PDF</html>'
        pdf = PDF(
            template_name='pdf.html',
            title='Awesome PDF'
        )
        pdf.add_page(template_name='pdf_page.html')
        html = pdf.render_html()
        mock_render_pdf_to_string.assert_called_once_with(
            template_name='pdf.html',
            context={
                'pages_html': '<div>PDF Page</div>',
                'title': 'Awesome PDF'
            }
        )
        self.mock_render_page_html.assert_called_once()
        self.assertEqual(html, '<html>PDF</html>')

    @patch('django_pdf_view.pdf.from_string')
    def test_in_memory_pdf(self, mock_from_string):
        mock_from_string.return_value = b'PDF content'
        pdf = PDF(template_name='django_pdf_view/pdf.html')
        pdf.add_page(template_name='django_pdf_view/pdf_page.html')
        in_memory_pdf = pdf.in_memory_pdf
        self.assertIsInstance(in_memory_pdf, BytesIO)
        self.assertEqual(in_memory_pdf.getvalue(), b'PDF content')

    def test_filename(self):
        """
        When the filename is provided, it should be returned.
        When the filename is not provided, the template name
        should be used to generate the filename.
        """
        named_pdf = PDF(template_name='pdf.html', filename='test.pdf')
        self.assertEqual(named_pdf.get_filename(), 'test.pdf')
        self.assertEqual(named_pdf.filename, 'test.pdf')

        nameless_pdf = PDF(template_name='document.html')
        self.assertEqual(nameless_pdf.get_filename(), 'document.pdf')
        self.assertEqual(nameless_pdf.filename, 'document.pdf')

    def test_get_title(self):
        """
        When the title is provided, it should be returned.
        When the title is not provided, the template name
        should be used to generate the title.
        """
        pdf = PDF(template_name='pdf.html', title='Custom Title')
        self.assertEqual(pdf.get_title(), 'Custom Title')

        pdf_without_title = PDF(template_name='document.html')
        self.assertEqual(pdf_without_title.get_title(), 'document')

    def test_get_context(self):
        pdf = PDF(template_name='pdf.html')
        pdf.add_page(template_name='pdf_page.html')
        context = pdf.get_context()
        self.assertEqual(context, {
            'pages_html': '<div>PDF Page</div>',
            'title': 'pdf'
        })

    def tearDown(self):
        super().tearDown()
        self.render_page_html_patcher.stop()
