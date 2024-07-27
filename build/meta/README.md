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

## Try it out

1. Add the following URL pattern to your project's `urls.py`:

   ```python
   from django.urls import path
   from django_pdf import views
   
   urlpatterns = [
       path(
           'singlepage-pdf/',
           views.SinglepageExamplePDFView.as_view(),
           name='singlepage_pdf'
       ),
       path(
           'multipage-pdf/',
           views.MultipageExamplePDFView.as_view(),
           name='multipage_pdf'
       ),
   ]
   ```
    <br/>

2. Run the development server:

   ```bash
   python manage.py runserver
   ```
   <br/>

3. Visit PDF examples in your browser:
    - Singlepage PFD: [http://127.0.0.1:8000/singlepage-pdf](http://127.0.0.1:8000/singlepage-pdf)
    - Multipage PFD: [http://127.0.0.1:8000/multipage-pdf](http://127.0.0.1:8000/multipage-pdf)
    - Append `?html=true` to the URL to view the HTML content.
    - Append `?download=true` to the URL to download the PDF file.

## Usage

In order to create your own PDFs, you need to implement
your own template and view.

1. Create a new template to define the content of your PDF page:

   ```html
   <!-- my_app/templates/my_app/pdf_page.html -->
   
   <style>
       {{ 'my_app/style/pdf_page.css'|css }}
   </style>
   
   <h1 class=".my-title">{{ title }}</h1>
   <p class=".my-text">{{ text }}</p>
   <p class=".my-text">Additional PDF page text.</p>
   ```
   **_Breakdown_**:
    - We render the content of a custom CSS file
      (`my_app/style/pdf_page.css`) in the `<style>` tag.
    - We define the content of our PDF page using HTML tags.
      Some of this content is passed as context to the template
      (variables `title` and `text`).
    - We use the `my-title` and `my-text` classes to style our
      content. These classes are defined in the custom CSS file
      (`my_app/static/my_app/style/pdf_page.css`) that we rendered
      in the `<style>` tag.
      <br/><br/>

2. Create a new view to render the PDF:

   ```python
   # my_app/views.py
   
   from django_pdf.pdf import PDF
   from django_pdf.services import create_pdf
   from django_pdf.views.pdf_view import PDFView
   
   
   class MyPDFView(PDFView):
   
        def create_pdf(self) -> PDF:
            return create_pdf(
                template_name='my_app/pdf_page.html',
                title='My PDF',
                context={
                    'title': 'My PDF Single Page Title',
                    'text': 'My PDF Single Page Text',
                }
            )
   ```
   **_Breakdown_**:
    - We create a new view class `MyPDFView` that extends `PDFView`.
    - We implement abstract method `create_pdf` to return a simple
      single-page PDF object by providing a `template_name` for the
      PDF page, a `title` (optional) for the PDF document, and a
      `context` (optional) for the PDF page template.
      <br/><br/>

3. Add the new URL pattern to your project's `urls.py`:

   ```python
   from django.urls import path
   from my_app.views import MyPDFView
   
   urlpatterns = [
        ...
        path('my_pdf/', MyPDFView.as_view(), name='my_pdf'),
        ...
   ]
   ```
   <br/>

4. Visit [http://localhost:8000/my_pdf/](http://localhost:8000/my_pdf/)
   in your browser.
    - To download the PDF, append `?download=true` to the URL:
      [http://localhost:8000/my_pdf/?download=true](http://localhost:8000/my_pdf/?download=true)
    - To view the HTML version, append `?html=true` to the URL:
      [http://localhost:8000/my_pdf/?html=true](http://localhost:8000/my_pdf/?html=true)
      <br/><br/>
