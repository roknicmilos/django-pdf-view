from django.test import TestCase
from django.utils import translation

from django_pdf_view.services import create_pdf


class TestCreatePDF(TestCase):

    def test_create_pdf_with_minimal_arguments(self):
        pdf = create_pdf(
            template_name='django_pdf_view/examples/singlepage.html'
        )

        self.assertEqual(pdf.template_name, 'django_pdf_view/pdf.html')
        self.assertEqual(pdf.get_title(), 'pdf')
        self.assertEqual(pdf.get_filename(), 'pdf.pdf')
        self.assertEqual(pdf.language, translation.get_language())

        self.assertEqual(len(pdf.pages), 1)
        page = pdf.pages[0]
        self.assertEqual(
            page.template_name,
            'django_pdf_view/examples/singlepage.html'
        )
        self.assertEqual(page.number, 1)
        self.assertEqual(page.get_context(), {'page_number': 1})
        self.assertTrue(page.with_wrapper_html)

    def test_create_pdf_with_all_arguments(self):
        pdf = create_pdf(
            template_name='django_pdf_view/examples/singlepage.html',
            title='My PDF',
            filename='my_pdf.pdf',
            context={'key': 'value'},
            language='rs',
        )

        self.assertEqual(pdf.template_name, 'django_pdf_view/pdf.html')
        self.assertEqual(pdf.get_title(), 'My PDF')
        self.assertEqual(pdf.get_filename(), 'my_pdf.pdf')
        self.assertEqual(pdf.language, 'rs')

        self.assertEqual(len(pdf.pages), 1)
        page = pdf.pages[0]
        self.assertEqual(
            page.template_name,
            'django_pdf_view/examples/singlepage.html'
        )
        self.assertEqual(page.number, 1)
        self.assertEqual(page.get_context(), {
            'key': 'value',
            'page_number': 1,
        })
        self.assertTrue(page.with_wrapper_html)
