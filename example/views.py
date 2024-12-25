from django.contrib import messages

from pdf_view.views import PDFView


class SinglePageExamplePDFView(PDFView):
    template_name = 'example/single_page.html'
    title = 'Single Page Example PDF'
    filename = 'single_page_example_pdf.pdf'
    css_paths = [
        'example/css/single_page.css',
        'example/css/flash_message.css',
    ]

    def get(self, *args, **kwargs):
        message = (
            'You are viewing the HTML version of the single page example PDF.'
        )
        messages.info(request=self.request, message=message)
        return super().get(*args, **kwargs)


class MultiPageExamplePDFView(PDFView):
    template_name = 'example/multi_page.html'
    title = 'Multi Page Example PDF'
    filename = 'multi_page_example_pdf.pdf'
    css_paths = [
        'example/css/multi_page.css',
        'example/css/flash_message.css',
    ]

    def get(self, *args, **kwargs):
        message = (
            'You are viewing the HTML version of the multi page example PDF.'
        )
        messages.info(request=self.request, message=message)
        return super().get(*args, **kwargs)
