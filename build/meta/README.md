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
    from django_pdf.views import ExamplePDFView

    urlpatterns = [
        ...
        path('pdf/', ExamplePDFView.as_view(), name='pdf'),
        ...
    ]
    ```
    <br/>

2. Run the development server:

   ```bash
   python manage.py runserver
   ```
   <br/>

3. Visit [http://localhost:8000/pdf/](http://localhost:8000/pdf/)
   in your browser.
    - To download the PDF, append `?download=true` to the URL:
      [http://localhost:8000/pdf/?download=true](http://localhost:8000/pdf/?download=true)
    - To view the HTML version, append `?html=true` to the URL:
      [http://localhost:8000/pdf/?html=true](http://localhost:8000/pdf/?html=true)

## Usage

In order to create your own PDFs, you need to implement
your own templates and view.

1. Create a new base template to include your custom CSS:

    ```html
    <!-- my_app/templates/my_app/pdf.html -->

    {% extends 'django_pdf/pdf.html' %}
    
    {% load css %}
    
    {% block style %}
        {{ block.super }}
        {{ 'my_app/style/pdf.css'|css }}
    {% endblock style %}

    ```
   **_Breakdown_**:
    - We extend the base `django_pdf/pdf.html` template to inherit
      the basic structure and CSS.
    - We load the `css` template tag that comes with `django_pdf`
      to include our own CSS files.
    - We override the `style` block to include our custom CSS file.
      <br/><br/>

2. Create a new template to define the content of your PDF page:

    ```html
    <!-- my_app/templates/my_app/pdf_page.html -->

    {% extends 'django_pdf/pdf_page.html' %}
    
    {% block content %}
        <h1 class=".my-title">{{ title }}</h1>
        <p class=".my-text">{{ text }}</p>
        <p class=".my-text">Additional PDF page text.</p>
    {% endblock content %}
    ```
   **_Breakdown_**:
    - We extend the base `django_pdf/pdf_page.html` template to inherit
      the basic structure and CSS.
    - We override the `content` block to include our custom content.
      Some of this content is passed as context to the template
      (variables `title` and `text`).
    - We use the `my-title` and `my-text` classes to style our content.
      These classes are defined in the custom CSS file
      (`my_app/static/my_app/style/pdf.css`) we included in the base
      template (`my_app/templates/my_app/pdf.html`).
      <br/><br/>

3. Create a new view to render the PDF:

   ```python
   # my_app/views.py
   
   from django_pdf.pdf import PDF
   from django_pdf.views.pdf_view import PDFView
   
   
   class MyPDFView(PDFView):
   
      def create_pdf(self) -> PDF:
           pdf = PDF(
                template_name='my_app/pdf.html',
                title='My PDF',
                filename='my_pdf.pdf',
           )
   
           pdf.add_page(
                template_name='my_app/pdf_page.html',
                title='My PDF Page',
                text='This is my PDF page text.',
           )
   
           return pdf
   ```
   **_Breakdown_**:
    - We create a new view class `MyPDFView` that extends `PDFView`.
    - We implement abstract method `create_pdf` to define the content of
      our PDF.
    - We create a new `PDF` object with `template_name`. Arguments `title`
      and `filename` are optional, which will default to template name if
      not provided.
    - We add a new page to the PDF by specifying a `template_name`. Every
      other argument is optional and will be passed as context to the template.
      <br/><br/>

4. Add the new URL pattern to your project's `urls.py`:

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

5. Visit [http://localhost:8000/my_pdf/](http://localhost:8000/my_pdf/)
   in your browser.
    - To download the PDF, append `?download=true` to the URL:
      [http://localhost:8000/my_pdf/?download=true](http://localhost:8000/my_pdf/?download=true)
    - To view the HTML version, append `?html=true` to the URL:
      [http://localhost:8000/my_pdf/?html=true](http://localhost:8000/my_pdf/?html=true)
      <br/><br/>
