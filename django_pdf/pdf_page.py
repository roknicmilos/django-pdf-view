from django.template.loader import render_to_string


class PDFPage:

    def __init__(
        self,
        template_name: str,
        number: int,
        context: dict = None,
    ):
        self.template_name = template_name
        self.number = number
        self.context = context or {}

    def render_html(self) -> str:
        return render_to_string(
            template_name=self.template_name,
            context=self.get_context()
        )

    def get_context(self) -> dict:
        return {
            **self.context,
            'page_number': self.number,
        }
