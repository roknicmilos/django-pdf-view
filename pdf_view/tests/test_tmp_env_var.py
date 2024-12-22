import os

from django.test import TestCase

from pdf_view.context_managers import tmp_env_var


class TestTmpEnvVar(TestCase):

    def test_set_new_env_var(self):
        key = 'TEST_ENV_VAR'
        value = 'test_value'

        if key in os.environ:
            del os.environ[key]

        with tmp_env_var(key, value):
            self.assertEqual(os.environ[key], value)

        self.assertNotIn(key, os.environ)

    def test_override_existing_env_var(self):
        key = 'TEST_ENV_VAR'
        original_value = 'original_value'
        new_value = 'new_value'

        os.environ[key] = original_value

        with tmp_env_var(key, new_value):
            self.assertEqual(os.environ[key], new_value)

        self.assertEqual(os.environ[key], original_value)
