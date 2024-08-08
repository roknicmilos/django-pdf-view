from django.test import TestCase
from unittest.mock import patch, mock_open

from django_pdf_view.templatetags.svg import svg


class TestSvgTemplateTag(TestCase):

    @patch(target='django_pdf_view.templatetags.svg.finders.find')
    def test_svg_file_found(self, mock_finders_find):
        mock_finders_find.return_value = '/path/to/static/file.svg'
        mocked_file_content = '<svg></svg>'
        with patch(
            target='builtins.open',
            new=mock_open(read_data=mocked_file_content)
        ) as mock_file:
            result = svg('file.svg')
            mock_file.assert_called_once_with('/path/to/static/file.svg', 'r')
            self.assertEqual(result, mocked_file_content)

    @patch(
        target='django_pdf_view.templatetags.svg.finders.find',
        return_value=None
    )
    def test_svg_file_not_found(self, _):
        with self.assertRaises(FileNotFoundError):
            svg('nonexistent.svg')

    def test_svg_invalid_extension(self):
        with self.assertRaises(ValueError):
            svg('file.txt')
