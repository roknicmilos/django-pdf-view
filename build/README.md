# Release a new django-pdf-view version

When changes are made to the `django_pdf_view` app that need
to be reflected in the published package, or some metadata
needs to be updated (`build/meta/*` files), a **new package
version should be built and uploaded to PyPI**.

Follow these steps to build and upload a new package version:

1. Install the necessary packages:
   ```bash
   python -m pip install -U wheel twine setuptools
   ```

2. Make sure you update the version number in `pyproject.toml`
   (e.g. `version = "1.1.0"` => `version = "1.1.1"`)
   <br/><br/>

3. Run `build/generate_src.py` to update the source files
   in the `build/src/` directory.
   <br/><br/>

4. Run `python -m build` to build source and binary
   distributions.
   <br/><br/>

5. Run `twine upload dist/*` to upload the new version
   to PyPI.
   <br/><br/>
