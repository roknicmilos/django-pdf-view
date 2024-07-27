from django_pdf_view.pdf import PDF


def create_pdf(
    template_name: str,
    title: str = None,
    filename: str = None,
    context: dict = None,
    language: str = None,
) -> PDF:
    """
    Creates a PDF object with a single page.
    """
    pdf = PDF(
        title=title,
        filename=filename,
        language=language
    )
    pdf.add_page(template_name=template_name, context=context)

    return pdf
