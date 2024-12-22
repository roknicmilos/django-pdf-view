from unittest.mock import patch, mock_open as open_mock
from django.test import SimpleTestCase

from pdf_view.utils import render_css


class TestRenderCss(SimpleTestCase):

    def setUp(self):
        super().setUp()

        self.finders_find_patcher = patch(
            target='pdf_view.utils.finders.find'
        )
        self.mock_finders_find = self.finders_find_patcher.start()

    def test_css_file_found(self):
        self.mock_finders_find.return_value = '/path/to/static/file.css'
        mocked_file_content = 'body { background-color: #fff; }'
        with patch(
            target='builtins.open',
            new=open_mock(read_data=mocked_file_content)
        ) as mock_file:
            result = render_css('file.css')
            mock_file.assert_called_once_with('/path/to/static/file.css', 'r')
            self.assertEqual(result, mocked_file_content)

    @patch(
        target='builtins.open',
        new_callable=open_mock,
        read_data='body { color: black; }'
    )
    @patch(target='os.walk')
    @patch(target='os.path.isdir', return_value=True)
    def test_get_dir_css_content(self, _, mock_walk, mock_open):
        mock_walk.return_value = [
            ('/fake_dir', ('subdir',),
             ('style1.css', 'style2.css', 'not_a_css.txt')),
            ('/fake_dir/subdir', (), ('sub_style.css',))
        ]

        expected_content = (
            'body { color: black; }\n'
            'body { color: black; }\n'
            'body { color: black; }\n'
        )

        result = render_css('/fake_dir')

        self.assertEqual(result, expected_content)

        mock_open.assert_any_call('/fake_dir/style1.css', 'r')
        mock_open.assert_any_call('/fake_dir/style2.css', 'r')
        mock_open.assert_any_call('/fake_dir/subdir/sub_style.css', 'r')

        self.assertEqual(mock_open.call_count, 3)

    def test_css_file_not_found(self):
        self.mock_finders_find.return_value = None
        with self.assertRaises(FileNotFoundError):
            render_css('nonexistent.css')

    def test_css_invalid_extension(self):
        with self.assertRaises(ValueError):
            render_css('file.txt')

    def tearDown(self):
        super().tearDown()
        self.finders_find_patcher.stop()
