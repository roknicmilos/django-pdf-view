import os

from django.test import TestCase

from django_pdf_view.utils import temporary_env_var


class TestTemporaryEnvVar(TestCase):

    def test_set_new_env_var(self):
        key = 'TEST_ENV_VAR'
        value = 'test_value'

        if key in os.environ:
            del os.environ[key]

        with temporary_env_var(key, value):
            self.assertEqual(os.environ[key], value)

        self.assertNotIn(key, os.environ)

    def test_override_existing_env_var(self):
        key = 'TEST_ENV_VAR'
        original_value = 'original_value'
        new_value = 'new_value'

        os.environ[key] = original_value

        with temporary_env_var(key, new_value):
            self.assertEqual(os.environ[key], new_value)

        self.assertEqual(os.environ[key], original_value)
