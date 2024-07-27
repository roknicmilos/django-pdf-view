from io import BytesIO

from django.template.loader import render_to_string
from django.utils import translation
from pdfkit import from_string

from django_pdf_view.pdf_page import PDFPage
from django_pdf_view.utils import override_language


class PDF:
    page_class = PDFPage
    default_template_name = 'django_pdf_view/pdf.html'

    def __init__(
        self,
        template_name: str = default_template_name,
        language: str = None,
        filename: str = None,
        title: str = None,
    ):
        self.template_name = template_name
        self.language = language or translation.get_language()
        self._filename = filename
        self._title = title
        self._pages = []
        self._in_memory_pdf = None

    def add_page(
        self,
        template_name: str,
        context: dict = None,
        with_wrapper_html: bool = True,
    ) -> None:
        page_number = len(self._pages) + 1
        new_page = self.page_class(
            template_name=template_name,
            number=page_number,
            context=context,
            with_wrapper_html=with_wrapper_html,
        )
        self._pages.append(new_page)

    @property
    def pages(self) -> list[PDFPage]:
        self._pages.sort(key=lambda page: page.number)
        return self._pages

    @property
    def filename(self) -> str:
        return self.get_filename()

    @override_language
    def get_filename(self) -> str:
        if self._filename:
            return self._filename
        return self.template_name.split('/')[-1].replace('.html', '.pdf')

    @override_language
    def render_html(self) -> str:
        return render_to_string(
            template_name=self.template_name,
            context=self.get_context()
        )

    def get_context(self) -> dict:
        total_pages = len(self._pages)
        pages_html = ''.join([
            page.render_html(total_pages=total_pages) for page in self.pages
        ])
        return {
            'pages_html': pages_html,
            'title': self.get_title(),
        }

    def get_title(self) -> str:
        title = self._title or self.filename
        if title.endswith('.pdf'):
            title = title[:-4]
        return title

    @property
    def in_memory_pdf(self) -> BytesIO:
        if not self._in_memory_pdf:
            html = from_string(self.render_html())
            self._in_memory_pdf = BytesIO(html)
        return self._in_memory_pdf
