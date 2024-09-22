# Working on the "Django PDF View" Project

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

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Run the Development Server**:
   ```bash
    poetry run python manage.py runserver
   ```

4. **Open PDF examples in the Browser**:
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

## Publishing to PyPI

To publish the package to PyPI, follow these steps:

1. Update the version in the `pyproject.toml` file.
   <br/><br/>

2. Build the package:
    ```bash
    poetry build
    ```
3. Configure your PyPI credentials (if you haven't already):

    ```bash
    poetry config pypi-token.pypi <your-pypi-token>
    ```
4. Publish the package:

    ```bash
    poetry publish
    ```