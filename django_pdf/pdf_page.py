from django.template.loader import render_to_string


class PDFPage:

    def __init__(
        self,
        template_name: str,
        number: int,
        context: dict = None,
        with_wrapper_html: bool = True,
    ):
        self.template_name = template_name
        self.number = number
        self.context = context or {}
        self.with_wrapper_html = with_wrapper_html

    def render_html(self, **extra_context) -> str:
        html = render_to_string(
            template_name=self.template_name,
            context=self.get_context(**extra_context)
        )
        if self.with_wrapper_html:
            return (
                f'<div class="pdf-page pdf-page--{self.number}">'
                f'{html}'
                '</div>'
            )
        return html

    def get_context(self, **extra_context) -> dict:
        return {
            **self.context,
            'page_number': self.number,
            **extra_context,
        }
