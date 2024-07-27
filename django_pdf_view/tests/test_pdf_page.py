from unittest import TestCase
from unittest.mock import patch

from django_pdf_view.pdf_page import PDFPage


class TestPDFPage(TestCase):

    def test_initialization(self):
        # Without context:
        pdf_page = PDFPage(
            template_name='pdf_page.html',
            number=1,
        )
        self.assertEqual(pdf_page.template_name, 'pdf_page.html')
        self.assertEqual(pdf_page.number, 1)
        self.assertEqual(pdf_page.context, {})

        # With context:
        pdf_page = PDFPage(
            template_name='pdf_page.html',
            number=1,
            context={'foo': 'bar'}
        )
        self.assertEqual(pdf_page.template_name, 'pdf_page.html')
        self.assertEqual(pdf_page.number, 1)
        self.assertEqual(pdf_page.context, {'foo': 'bar'})

    @patch('django_pdf_view.pdf_page.render_to_string')
    def test_render_html_with_wrapper_html(self, mock_render_pdf_to_string):
        """
        If with_wrapper_html is True (default), render_html should
        return the rendered template wrapped in a div with the class
        'pdf-page' and 'pdf-page--{page_number}'.
        """
        mock_render_pdf_to_string.return_value = '<html>PDF Page</html>'
        pdf_page = PDFPage(
            template_name='pdf_page.html',
            number=1,
            context={'foo': 'bar'}
        )
        html = pdf_page.render_html()
        expected_html = (
            '<div class="pdf-page pdf-page--1">'
            '<html>PDF Page</html>'
            '</div>'
        )
        self.assertEqual(html, expected_html)

    @patch('django_pdf_view.pdf_page.render_to_string')
    def test_render_html_without_wrapper_html(self, mock_render_pdf_to_string):
        """
        If with_wrapper_html is False, render_html should return the
        rendered template without any wrapping.
        """
        mock_render_pdf_to_string.return_value = '<html>PDF Page</html>'
        pdf_page = PDFPage(
            template_name='pdf_page.html',
            number=1,
            context={'foo': 'bar'},
            with_wrapper_html=False,
        )
        html = pdf_page.render_html()
        self.assertEqual(html, mock_render_pdf_to_string.return_value)

    def test_get_context(self):
        pdf_page = PDFPage(
            template_name='pdf_page.html',
            number=1,
            context={'foo': 'bar'}
        )
        context = pdf_page.get_context(bar='baz')
        self.assertEqual(context, {
            'foo': 'bar',
            'page_number': 1,
            'bar': 'baz',
        })
