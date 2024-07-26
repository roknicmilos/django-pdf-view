# django-pdf

**Django PDF** is a Django app with classes, views, and
templates for creating and displaying PDFs in the browser or
downloading them based on URL parameters.

## Prerequisites

- [wkhtmltopdf](https://wkhtmltopdf.org/)
    - Linux:
        ```bash
        sudo apt-get install wkhtmltopdf
        ``` 
    - macOS:
        ```bash
        brew install wkhtmltopdf
        ```
    - Windows: Download the installer from the
      [wkhtmltopdf website](https://wkhtmltopdf.org/)

## Installation

```bash
pip install django-pdf
```

## Configuration

Add `django-pdf` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_pdf',
    ...
]
```
