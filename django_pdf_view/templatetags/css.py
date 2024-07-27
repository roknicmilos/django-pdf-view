from django.contrib.staticfiles import finders
from django import template

register = template.Library()


@register.filter
def css(filepath: str) -> str:
    """
    Returns the content of a CSS file.
    """

    if not filepath.endswith('.css'):
        raise ValueError('The file path must end with ".css"')

    if absolute_path := finders.find(filepath):
        with open(absolute_path, 'r') as file:
            return file.read()

    raise FileNotFoundError(f"Static file '{filepath}' not found.")
