# Django PDF View

[![Build Status](https://github.com/roknicmilos/django-pdf-view/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/roknicmilos/django-pdf-view/actions/workflows/ci.yml/?query=branch:main)
[![PyPI version](https://img.shields.io/pypi/v/django-pdf-view.svg)](https://pypi.org/project/django-pdf-view/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/roknicmilos/django-pdf-view.svg)](https://github.com/roknicmilos/django-pdf-view/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/roknicmilos/django-pdf-view.svg)](https://github.com/<username>/<repository>/issues)

**NOTE**: This is a full Django project that demonstrates the
usage of the [django-pdf-view](https://pypi.org/project/django-pdf-view/)
package.
It is also used for development and testing of the package.
If you want to install Django PDF View as a standalone package in
your Django project, refer to the official
[documentation](https://pypi.org/project/django-pdf-view/).

## Purpose

The primary purpose of this package is to streamline the creation of
PDF documents and displaying those PDFs in the browser or downloading
them based on URL parameters. The package provides a **robust
foundation of HTML and CSS for PDF page(s) layout**.
Simply create an HTML template(s) for your PDF page(s), then define
a view that inherits from `PDFView` and implements the `create_pdf`
method that returns a PDF object with the desired content.
This allows developers to focus on defining the content and custom
styles of their PDF pages without worrying about the underlying layout
complexities.

### Key Features

- **Predefined Page Layout**: The package includes built-in HTML
  and CSS for structuring PDF pages.

- **Flexible PDF Content and Styling**: Easily create your own HTML
  templates for PDF pages and customize the look of your PDFs by
  providing your own CSS.

- **PDF View**: Easily switch between viewing the PDF, HTML content
  and downloading the PDF file by appending URL parameters.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) 3.10 or higher
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

### Setup and Running Instructions

1. **Clone the Project**:
   ```bash
   git clone <repository-url>
   cd django-pdf-view
   ```

2. **Create and activate Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements/dev.txt
   ```

4. **Run Migrations**:
   ```bash
   python3 manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python3 manage.py runserver
   ```

6. **Open PDF examples in the Browser**:
    - Singlepage
      example: [http://127.0.0.1:8000/singlepage-example](http://127.0.0.1:8000/singlepage-example)
    - Multipage
      example: [http://127.0.0.1:8000/multipage-example](http://127.0.0.1:8000/multipage-example)
    - Append `?html=true` to the URL to view the HTML content.
    - Append `?download=true` to the URL to download the PDF file.

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## Bugs/Requests

If you encounter any bugs or have any requests, please use
[GitHub issue tracker](https://github.com/roknicmilos/django-pdf-view/issues)
to report them.

# Release a new version

When changes are made to the [django_pdf_view](./django_pdf_view) app that
need to be reflected in the published package, or some package metadata was
changed (in [meta/](./meta) directory), a **new package version should be
created and published**.

To create and publish a new package version, run the following commands:

```bash
chmod +x -R ./scripts/
./scripts/release
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
