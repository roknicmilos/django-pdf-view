import pytest
from django.conf import settings
from django.test.utils import (
    setup_test_environment,
    teardown_test_environment,
)


@pytest.fixture(scope='session', autouse=True)
def django_test_environment():
    """
    Sets up and tears down the Django test environment.
    This fixture is automatically used for all tests.
    """
    setup_test_environment()
    settings.DEBUG = False
    yield
    teardown_test_environment()
