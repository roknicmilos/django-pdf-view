from unittest import TestCase
from unittest.mock import patch
from io import BytesIO

from django.template.loader import render_to_string

from pdf_view.pdf import PDF
from pdf_view.utils import render_css


class TestPDF(TestCase):

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

    @patch('pdf_view.pdf.PDF.get_context')
    def test_render_html(self, mock_get_context):
        pdf = PDF(
            template_name='pdf.html',
            title='Awesome PDF'
        )
        mock_get_context.return_value = {}
        actual_html = pdf.render_html()
        expected_html = render_to_string(
            template_name='pdf_view/pdf.html',
            context=mock_get_context.return_value
        )
        self.assertEqual(actual_html, expected_html)

    @patch('pdf_view.pdf.from_string')
    def test_in_memory_pdf(self, mock_from_string):
        mock_from_string.return_value = b'PDF content'
        pdf = PDF(template_name='pdf_view/pdf.html')
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

    @patch('pdf_view.pdf.render_to_string')
    def test_get_context(self, mock_render_to_string):
        mock_render_to_string.return_value = 'content'
        extra_context = {
            'extra': 'context'
        }
        pdf = PDF(
            template_name='pdf.html',
            context=extra_context
        )
        context = pdf.get_context()
        self.assertEqual(context, {
            'content': mock_render_to_string.return_value,
            'title': 'pdf',
            'css': render_css('pdf_view/css/pdf.css'),
            **extra_context,
        })
