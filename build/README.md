# Release a new django-pdf-view version

When changes are made to the `django_pdf_view` app that need
to be reflected in the published package, or some package
metadata was changed (`build/meta/*` files), a **new package
version should be built and uploaded to PyPI**.

Follow these steps to build and upload a new package version:

1. Install the necessary packages:
   ```bash
   python3 -m pip install -U wheel twine setuptools
   ```

2. Make sure you update the version number in `pyproject.toml`
   (e.g. `version = "1.1.0"` => `version = "1.1.1"`)
   <br/><br/>

3. To package the app and create a new distribution, run:
   ```bash
    sh build.sh
    ```
    - Optionally, you add `--push-test` or `--push-main` to
      the command to automatically push the new version to the
      test or main PyPI repository.
      <br/><br/>
