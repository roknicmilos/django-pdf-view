from io import BytesIO

from django.template.loader import render_to_string
from django.utils import translation
from pdfkit import from_string

from django_pdf_view.decorators import override_language
from django_pdf_view.utils import render_css


class PDF:

    def __init__(
        self,
        template_name: str,
        base_template_name: str = 'django_pdf_view/pdf.html',
        language: str = None,
        filename: str = None,
        title: str = None,
        context: dict = None,
        css_paths: list = None,  # file or directory paths
    ):
        self.template_name = template_name
        self.base_template_name = base_template_name
        self.language = language or translation.get_language()
        self._filename = filename
        self._title = title
        self._context = context or {}
        self._css_paths = css_paths or []
        # Add the base CSS path to the beginning of the list:
        self._css_paths.insert(0, 'django_pdf_view/css/pdf.css')
        self._in_memory_pdf = None

    @property
    def filename(self) -> str:
        return self.get_filename()

    @override_language
    def get_filename(self) -> str:
        if self._filename:
            return self._filename

        # Use the template name as default filename:
        return self.template_name.split('/')[-1].replace('.html', '.pdf')

    @override_language
    def render_html(self) -> str:
        return render_to_string(
            template_name=self.base_template_name,
            context=self.get_context()
        )

    def get_context(self) -> dict:
        css = '\n'.join(render_css(css_path) for css_path in self._css_paths)
        context = {
            'title': self.get_title(),
            'css': css,
            **self._context,
        }
        content = render_to_string(
            template_name=self.template_name,
            context=context,
        )
        return {
            'content': content,
            **context
        }

    def get_title(self) -> str:
        title = self._title or self.filename
        if title.endswith('.pdf'):
            title = title[:-4]
        return title

    @property
    def in_memory_pdf(self) -> BytesIO:
        if not self._in_memory_pdf:
            html = from_string(
                input=self.render_html(),
                options={
                    'page-size': 'A4',
                    'margin-top': '0mm',
                    'margin-right': '0mm',
                    'margin-bottom': '0mm',
                    'margin-left': '0mm',
                    'dpi': '300',
                }
            )
            self._in_memory_pdf = BytesIO(html)
        return self._in_memory_pdf
