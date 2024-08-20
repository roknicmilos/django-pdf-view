import os
from django.contrib.staticfiles import finders


def render_css(path: str) -> str:
    """
    Returns the content of a CSS file or all CSS files in a directory.
    """

    if not (path.endswith('.css') or os.path.isdir(finders.find(path))):
        raise ValueError(
            'The path must end with ".css" or '
            'be a directory containing CSS files.'
        )

    absolute_path = finders.find(path)

    if not absolute_path:
        raise FileNotFoundError(f"Static file or directory '{path}' not found.")

    if os.path.isdir(absolute_path):
        return _get_dir_css_content(absolute_path)

    # If the path is a file, return its content.
    with open(absolute_path, 'r') as file:
        return file.read()


def _get_dir_css_content(dir_path: str) -> str:
    css_content = ''
    for root, _, files in os.walk(dir_path):
        for file in sorted(files):  # Sort files alphabetically
            if file.endswith('.css'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as css_file:
                    css_content += css_file.read() + '\n'

    return css_content
