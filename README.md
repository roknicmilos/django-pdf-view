# Django PDF View

**Django PDF View** is a Django project designed to generate
PDF files.
The project includes an application with classes, views, and
templates for creating and displaying PDFs in the browser or
downloading them based on URL parameters.

## Standalone Usage

If you want to install `django-pdf-view` as a standalone 
package in your Django project, refer to 
[build/meta/README.md](build/meta/README.md).

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
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements/dev.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Open PDF examples in the Browser**:
    - Singlepage example: [http://127.0.0.1:8000/pdf/singlepage-example](http://127.0.0.1:8000/pdf/singlepage-example)
    - Multipage example: [http://127.0.0.1:8000/pdf/multipage-example](http://127.0.0.1:8000/pdf/multipage-example)
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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
