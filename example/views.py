from django_pdf_view.views import PDFView


class SinglePageExamplePDFView(PDFView):
    template_name = 'example/single_page.html'
    title = 'Single Page Example PDF'
    filename = 'single_page_example_pdf.pdf'
    css_paths = [
        'example/css/single_page.css',
    ]


class MultiPageExamplePDFView(PDFView):
    template_name = 'example/multi_page.html'
    title = 'Multi Page Example PDF'
    filename = 'multi_page_example_pdf.pdf'
    css_paths = [
        'example/css/multi_page.css',
    ]
