# django-pdf-view

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

## Prerequisites

- [wkhtmltopdf](https://wkhtmltopdf.org/) command line tools to
  render HTML into PDF:
    ```bash
    sudo apt-get install wkhtmltopdf  # Linux
    ```
    ```bash
    brew install wkhtmltopdf          # macOS
    ```
  For Windows, download the installer from the
  [wkhtmltopdf website](https://wkhtmltopdf.org/).

## Installation

```bash
pip install django-pdf-view
```

## Configuration

Add `django-pdf-view` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_pdf_view',
    ...
]
```

## Try it out

1. Add the following URL pattern to your project's `urls.py`:

   ```python
   from django.urls import path
   from django_pdf_view import views
   
   urlpatterns = [
       path(
           'single-page-pdf/',
           views.SinglePageExamplePDFView.as_view(),
           name='single_page_pdf'
       ),
       path(
           'multi-page-pdf/',
           views.MultiPageExamplePDFView.as_view(),
           name='multi_page_pdf'
       ),
   ]
   ```
    <br/>

2. Run the development server:

   ```bash
   python3 manage.py runserver
   ```
   <br/>

3. Visit PDF examples in your browser:
    - Single Page PFD: [http://127.0.0.1:8000/single-page-pdf](http://127.0.0.1:8000/single-page-pdf)
    - Multi Page PFD: [http://127.0.0.1:8000/multi-page-pdf](http://127.0.0.1:8000/multi-page-pdf)
    - Append `?html=true` to the URL to view the HTML content.
    - Append `?download=true` to the URL to download the PDF file.

## Usage

In order to create your own PDFs, you need to implement
your own template and view.

1. Create a new template to define the content of your PDF page:

   ```html
   <!-- my_app/templates/my_app/pdf_page.html -->
   {% load css %}   
   
   <style>
       {{ 'my_app/style/pdf_page.css'|css }}
   </style>
   
   <h1 class="my-title">{{ title }}</h1>
   <p class="my-text">{{ text }}</p>
   <p class="my-text">Additional PDF page text.</p>
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
   
   from django_pdf_view.pdf import PDF
   from django_pdf_view.services import create_pdf
   from django_pdf_view.views.pdf_view import PDFView
   
   
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
        path('my-pdf/', MyPDFView.as_view(), name='my_pdf'),
        ...
   ]
   ```
   <br/>

4. Visit [http://localhost:8000/my-pdf/](http://localhost:8000/my-pdf/)
   in your browser.
    - To download the PDF, append `?download=true` to the URL:
      [http://localhost:8000/my-pdf/?download=true](http://localhost:8000/my-pdf/?download=true)
    - To view the HTML version, append `?html=true` to the URL:
      [http://localhost:8000/my-pdf/?html=true](http://localhost:8000/my-pdf/?html=true)
      <br/><br/>

## Advanced Usage

To have more control over the PDF generation process, instead of
using the `create_pdf` helper function, you can create a PDF object
manually and add pages to it:

```python
from django_pdf_view.pdf import PDF

pdf = PDF(
    template_name='my_app/pdf.html',
    title='My PDF Document',
    language='rs',
    filename='my-pdf.pdf',
)
# Add first page:
pdf.add_page(
    template_name='my_app/pdf_page_1.html',
    with_wrapper_html=False,
    context={
        'title': 'Page 1 Title',
        'text': 'Page 1 Text',
    }
)
# Add second page:
pdf.add_page(
    template_name='my_app/pdf_page_2.html',
    with_wrapper_html=False,
    context={
        'title': 'Page 2 Title',
        'text': 'Page 2 Text',
    }
)

```

**_Breakdown_**:

- We create a new `PDF` object with a custom `template_name` (optional)
  for the document, a `title` (optional) for the document, a `language`
  (optional) for the document, and a `filename` (optional) for the
  PDF file.
- We add two pages to the PDF object by providing a `template_name`
  for each page, `with_wrapper_html=False` (optional) to omit wrapper
  HTML that is added to each page, and a `context` (optional) for
  each page template.

### Default template context

- PDF document:
    - `pages_html`: HTML content of all pages.
    - `title`: Title of the PDF document (used in `<title>` tag).
- PDF page:
    - `title`: Title of the PDF page.
    - `page_number`: Number of the PDF page.
    - `total_pages`: Total number of pages in the PDF document.

### Template tags & filters

There are some useful template tags and filters provided by the
`django-pdf-view` package that can be used in your PDF templates:

- `css` template filter
    ```html
   {% load css %}   
       
   <style>
       {{ 'path/to/style.css'|css }}
   </style>
    ```
- `svg` template tag
    ```html
   {% load svg %}
   
   {% svg 'path/to/image.svg' %}
    ```

### Custom template for PDF document

If we decide to use our own template for the PDF document, we need
to include `{{ pages_html|safe }}` in the template to render the
content of the PDF pages.

### Custom CSS for PDF document

To add some global styles to the PDF document that will be
applied to all pages, we can define it directly in `<style>`
(inside `<head>` tag) in the PDF document template. Alternatively,
we can define it in a separate CSS file and render it in the
template using the `{{ 'my_app/style/pdf.css'|css }}` template tag.
