# django-pdf-view

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

## Prerequisites

- [wkhtmltopdf](https://wkhtmltopdf.org/)

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

## Usage

In order to create your own PDF, you need to implement your own view and
template.

1. Create a new view to render the PDF:

    ```python
   # my_app/views.py    
        
   from django_pdf_view.views.pdf_view import PDFView
        
        
   class MyPDFView(PDFView):
        template_name = 'my_app/my_pdf.html'
        title = 'My PDF Document' # optional
        filename = 'My PDF.pdf' # optional
        css_paths = [ # optional
            'my_pdf/css/my_pdf.css',
        ]
    ```

2. Create a new template to define the content of your PDF page:

   ```html
   <!-- my_app/templates/my_app/pdf_page.html -->
   
   <div class="page">
        <h1 class="my-title">{{ title }}</h1>
        <p class="my-text">{{ text }}</p>
        <p class="my-text">Additional PDF page text.</p>
   </div>
   
   <!-- Define more <div class="page"> elements for additional pages -->
   ```

3. Add the new URL patterns to your project's `urls.py`:

    ```python
    # my_app/urls.py    
    
    from django.urls import path
    from my_app.views import MyPDFView
    
    urlpatterns = [
        path('pdf-file/', MyPDFView.as_view(response_type='pdf'), name='pdf-file'),
        path('pdf-html/', MyPDFView.as_view(response_type='html'), name='pdf-html'),
        path('pdf-download/', MyPDFView.as_view(response_type='download'), name='pdf-download'),
    ]
    ```
   <br/>

4. Visit the belows listed URLs:

- To view the PDF
  file: [http://localhost:8000/pdf-file/](http://localhost:8000/pdf-file/)
- To view the
  HTML: [http://localhost:8000/pdf-html/](http://localhost:8000/pdf-html/)
- To download the PDF
  file: [http://localhost:8000/pdf-download/](http://localhost:8000/pdf-download/)

### Default template context

- PDF document:
    - `title`: Title of the PDF document (used in `<title>` tag).
    - `css`: Content of the CSS files specified in the `css_paths` attribute.
    - `content`: Content of the HTML template.
    - `response_type`: Type of the response (`pdf`, `html` or `download`).

### `svg` template tag

`svg` template tag is provided by the `django-pdf-view` package. This template
tag can be used to include SVG images in the PDF document.

**Usage example**:

```html
{% load svg %}

<!-- Some HTML content -->

{% svg 'path/to/image.svg' %}

<!-- Some more HTML content -->
```
