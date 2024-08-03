# Django PDF View

**Django PDF View** is a Django app that streamlines the process
of generating and displaying PDFs in the browser or downloading
them based on URL parameters.
Simply create an HTML template for your PDF document, then define
a view that inherits from `PDFView` and implements the `create_pdf`
method to return a PDF object with the desired content.

**NOTE**: This is a full Django project that demonstrates the 
usage of the **Django PDF View** package.
It is also used for development and testing of the package.
If you want to install Django PDF View as a standalone package in
your Django project, refer to the official
[Django PDF View documentation](https://pypi.org/project/django-pdf-view/)
at PyPI.

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
    - Singlepage example: [http://127.0.0.1:8000/singlepage-example](http://127.0.0.1:8000/singlepage-example)
    - Multipage example: [http://127.0.0.1:8000/multipage-example](http://127.0.0.1:8000/multipage-example)
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
