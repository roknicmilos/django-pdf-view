import re

from django.contrib.staticfiles import finders
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def svg(filepath: str, color: str = None) -> str:
    """
    Returns the content of an SVG file with an optional fill color.
    In order to change the color of an SVG, the SVG file must have
    the `data-dynamic-color="true"` attribute in the element that
    should change color.
    """

    if not filepath.endswith('.svg'):
        raise ValueError('The file path must end with ".svg"')

    if absolute_path := finders.find(filepath):
        with open(absolute_path, 'r') as file:
            original_svg = mark_safe(file.read())
        return mark_safe(
            _paint_svg(original_svg, color) if color else original_svg
        )

    raise FileNotFoundError(f'Static file "{filepath}" not found.')


def _paint_svg(original_svg: str, color: str) -> str:
    """
    Paints the SVG with the given color.
    """

    # Match elements with `data-dynamic-color="true"` and `fill="..."` after it,
    # and replace the `fill` attribute with the new color:
    painted_svg = re.sub(
        r'(<[^>]+data-dynamic-color="true"[^>]*?)\s*fill="[^"]*"',
        lambda match: f'{match.group(1)} fill="{color}"',
        original_svg,
    )

    # Match elements with `fill="..."` and `data-dynamic-color="true"`
    # after it, and replace the `fill` attribute with the new color:
    return re.sub(
        r'fill="[^"]*"\s*([^>]*\bdata-dynamic-color="true")',
        lambda match: f'{match.group(1)} fill="{color}"',
        painted_svg,
    )
