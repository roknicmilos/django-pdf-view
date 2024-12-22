from django.test import TestCase
from unittest.mock import patch, mock_open

from pdf_view.templatetags.svg import svg


class TestSvgTemplateTag(TestCase):

    @patch(target='pdf_view.templatetags.svg.finders.find')
    def test_svg_with_original_color(self, mock_finders_find):
        """
        Test that the original SVG is returned when no color is provided.
        """
        svg_file_path = '/path/to/static/file.svg'
        mock_finders_find.return_value = svg_file_path
        mocked_file_content = '<svg><path fill="red" /></svg>'
        with patch(
            target='builtins.open',
            new=mock_open(read_data=mocked_file_content)
        ) as mock_file:
            result = svg('file.svg')
            mock_file.assert_called_once_with(svg_file_path, 'r')
            self.assertEqual(result, mocked_file_content)

    @patch(target='pdf_view.templatetags.svg.finders.find')
    def test_svg_with_custom_color(self, mock_finders_find):
        """
        Test that the `fill` attribute of elements with
        `data-dynamic-color="true"` is updated with the provided color.
        """
        svg_file_path = '/path/to/static/file.svg'
        mock_finders_find.return_value = svg_file_path
        mocked_file_content = '''
            <svg>
                <path fill="red" data-dynamic-color="true" />
                <circle data-dynamic-color="true" fill="blue" />
                <circle fill="green" />
            </svg>
        '''
        custom_color = 'yellow'

        with patch(
            target='builtins.open',
            new=mock_open(read_data=mocked_file_content)
        ) as mock_file:
            result = svg('file.svg', custom_color)

        mock_file.assert_called_once_with(svg_file_path, 'r')
        expected_result = '''
            <svg>
                <path data-dynamic-color="true" fill="yellow" />
                <circle data-dynamic-color="true" fill="yellow" />
                <circle fill="green" />
            </svg>
        '''
        self.assertEqual(result, expected_result)

    @patch(
        target='pdf_view.templatetags.svg.finders.find',
        return_value=None
    )
    def test_svg_file_not_found(self, _):
        with self.assertRaises(FileNotFoundError):
            svg('nonexistent.svg')

    def test_svg_invalid_extension(self):
        with self.assertRaises(ValueError):
            svg('file.txt')
