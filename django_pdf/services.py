from django_pdf.pdf import PDF


def create_pdf(
    template_name: str,
    title: str = None,
    filename: str = None,
    context: dict = None,
    language: str = None,
) -> PDF:
    """
    Create a PDF object with a single page.
    """

    pdf = PDF(
        title=title,
        filename=filename,
        language=language
    )

    if context is None:
        context = {}

    pdf.add_page(template_name=template_name, **context)

    return pdf