from django.contrib.staticfiles import finders
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def svg(filepath: str) -> str:
    """
    Returns the content of an SVG file.
    """

    if not filepath.endswith('.svg'):
        raise ValueError('The file path must end with ".svg"')

    if absolute_path := finders.find(filepath):
        with open(absolute_path, 'r') as file:
            return mark_safe(file.read())

    raise FileNotFoundError(f'Static file "{filepath}" not found.')
