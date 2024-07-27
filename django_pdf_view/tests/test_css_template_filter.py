from unittest.mock import patch, mock_open
from django.test import SimpleTestCase

from django_pdf_view.templatetags.css import css


class TestCssTemplateFilter(SimpleTestCase):

    @patch(target='django_pdf_view.templatetags.css.finders.find')
    def test_css_file_found(self, mock_finders_find):
        mock_finders_find.return_value = '/path/to/static/file.css'
        mocked_file_content = 'body { background-color: #fff; }'
        with patch(
            target='builtins.open',
            new=mock_open(read_data=mocked_file_content)
        ) as mock_file:
            result = css('file.css')
            mock_file.assert_called_once_with('/path/to/static/file.css', 'r')
            self.assertEqual(result, mocked_file_content)

    @patch(
        target='django_pdf_view.templatetags.css.finders.find',
        return_value=None
    )
    def test_css_file_not_found(self, _):
        with self.assertRaises(FileNotFoundError):
            css('nonexistent.css')

    def test_css_invalid_extension(self):
        with self.assertRaises(ValueError):
            css('file.txt')
