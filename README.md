# Django PDF View

[![Build Status](https://github.com/roknicmilos/django-pdf-view/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/roknicmilos/django-pdf-view/actions/workflows/ci.yml/?query=branch:main)
[![PyPI version](https://img.shields.io/pypi/v/django-pdf-view.svg)](https://pypi.org/project/django-pdf-view/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/roknicmilos/django-pdf-view.svg)](https://github.com/roknicmilos/django-pdf-view/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/roknicmilos/django-pdf-view.svg)](https://github.com/<username>/<repository>/issues)

**NOTE**: This is a full Django project that demonstrates the usage of
the [django-pdf-view](https://pypi.org/project/django-pdf-view/) package.
It is also used for development and testing of the package. If you want to
install Django PDF View as a standalone package in your Django project, refer to
the official [documentation](https://pypi.org/project/django-pdf-view/).

## Purpose

The primary purpose of this Django package is to streamline the creation of PDF
documents and allow for easy viewing or downloading in the browser. The package
provides a **solid foundation of HTML and CSS for PDF file layout**. To use it,
simply create an HTML template for your PDF document, then create a view that
inherits from `PDFView` and define the necessary class attributes to generate
the PDF.

This approach enables developers to focus on crafting the content and styles of
their PDF pages without having to deal with complex layout issues.

### Key Features

- **Predefined Page Layout**: Includes built-in base HTML and CSS to help
  structure your PDF pages efficiently.

- **Flexible PDF Content and Styling**: Easily create your own HTML template for
  the PDF document and customize the appearance by applying your own CSS.

- **PDF View Response Options**: Seamlessly switch between viewing the PDF,
  displaying the HTML content, and downloading the PDF file.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) 3.10 or higher
- [wkhtmltopdf](https://wkhtmltopdf.org/)

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
    - Single Page
      examples:
        - [http://127.0.0.1:8000/examples/single-page/pdf](http://127.0.0.1:8000/examples/single-page/pdf/)
        - [http://127.0.0.1:8000/examples/single-page/html](http://127.0.0.1:8000/examples/single-page/html/)
        - [http://127.0.0.1:8000/examples/single-page/download](http://127.0.0.1:8000/examples/single-page/download/)
    - Multi Page examples:
        - [http://127.0.0.1:8000/examples/multi-page/pdf](http://127.0.0.1:8000/examples/multi-page/pdf/)
        - [http://127.0.0.1:8000/examples/multi-page/html](http://127.0.0.1:8000/examples/multi-page/html/)
        - [http://127.0.0.1:8000/examples/multi-page/download](http://127.0.0.1:8000/examples/multi-page/download/)

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
./scripts/release <major|minor|patch>
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
