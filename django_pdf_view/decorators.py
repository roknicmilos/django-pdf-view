from functools import wraps
from typing import Callable, Any
from django.utils import translation

from django_pdf_view.context_managers import tmp_env_var


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


def with_tmp_env_var(key: str, value: str) -> Callable:
    """
    Decorator that sets a temporary environment variable
    with the given key and value for the duration of the
    decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with tmp_env_var(key, value):
                return func(*args, **kwargs)

        return wrapper

    return decorator
