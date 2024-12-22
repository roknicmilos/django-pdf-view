import os
from django.test import TestCase

from pdf_view.decorators import with_tmp_env_var


class TestWithTmpEnvVar(TestCase):

    def test_existing_env_var_overridden_during_function_execution(self):
        os.environ['TEST_ENV_VAR'] = 'original_value'

        @with_tmp_env_var('TEST_ENV_VAR', 'temp_value')
        def test_function():
            self.assertEqual(os.environ['TEST_ENV_VAR'], 'temp_value')

        test_function()

        self.assertEqual(os.environ['TEST_ENV_VAR'], 'original_value')

    def test_new_env_var_set_during_function_execution(self):
        if 'TEST_ENV_VAR' in os.environ:
            del os.environ['TEST_ENV_VAR']

        @with_tmp_env_var('TEST_ENV_VAR', 'temp_value')
        def test_function():
            self.assertEqual(os.environ['TEST_ENV_VAR'], 'temp_value')

        test_function()

        self.assertNotIn('TEST_ENV_VAR', os.environ)
