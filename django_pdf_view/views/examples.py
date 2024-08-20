from django_pdf_view.views.pdf_view import PDFView


class SinglePageExamplePDFView(PDFView):
    template_name = 'django_pdf_view/examples/single_page.html'
    title = 'Single Page Example PDF'
    filename = 'single_page_example_pdf.pdf'
    css_paths = [
        'django_pdf_view/css/examples/single_page.css',
    ]


class MultiPageExamplePDFView(PDFView):
    template_name = 'django_pdf_view/examples/multi_page.html'
    title = 'Multi Page Example PDF'
    filename = 'multi_page_example_pdf.pdf'
    css_paths = [
        'django_pdf_view/css/examples/multi_page.css',
    ]
