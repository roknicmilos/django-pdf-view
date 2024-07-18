# Django PDF

**Django PDF** is a Django project designed to generate PDF files.
The project includes an application with classes, views, and
templates for creating and displaying PDFs in the browser or
downloading them based on URL parameters.

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
   cd django-pdf
   ```

2. **Create and activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Open Example PDF in the Browser**:
   [http://127.0.0.1:8000/pdf/example](http://127.0.0.1:8000/pdf/example)

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```
