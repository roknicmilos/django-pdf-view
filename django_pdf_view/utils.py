import os
from contextlib import contextmanager
from functools import wraps
from typing import Callable, Any
from django.utils import translation


def override_language(method: Callable) -> Callable:
    """
    Decorator that overrides the language of the current thread
    with the language of the instance of the class where the
    decorated method is called.
    """

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        language = self.language or translation.get_language()
        with translation.override(language):
            return method(self, *args, **kwargs)

    return wrapper


@contextmanager
def temporary_env_var(key, value):
    original_value = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if original_value is not None:
            os.environ[key] = original_value
        else:
            del os.environ[key]
