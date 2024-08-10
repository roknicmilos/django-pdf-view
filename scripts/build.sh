#!/bin/sh

# This script packages the django-pdf-view application.
# It prepares the source directory, copies necessary
# files, builds the distribution files, and checks the
# built distributions for correctness.
# Optionally, it can push the built distributions to
# PyPI or TestPyPI based on the flags provided.

show_usage() {
  echo "Usage: $0 [--push-main] [--push-test]"
  echo
  echo "Options:"
  echo "  --push-main   Push the built package to main PyPI."
  echo "  --push-test   Push the built package to test PyPI."
  echo "  -h, --help    Show this help message."
}

parse_arguments() {
  # Parse the first command-line argument if provided:
  if [ "$1" ]; then
    if [ "$1" = "--push-main" ]; then
      PUSH_MAIN=true
    elif [ "$1" = "--push-test" ]; then
      PUSH_TEST=true
    elif [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
      show_usage
      exit 1
    else
      echo "Unknown command: '$1'"
      show_usage
      exit 1
    fi
  fi
}

########################################################
############# Main script execution ####################
########################################################
# Initialize variables:
PUSH_MAIN=false
PUSH_TEST=false
THIS_SCRIPT=$(realpath "$0")
SCRIPTS_DIR=$(dirname "$THIS_SCRIPT")
ROOT_DIR=$(dirname "$SCRIPTS_DIR")
META_DIR="$ROOT_DIR/meta/"
SRC_DIR="$ROOT_DIR/src/"
DIST_DIR="$ROOT_DIR/dist/"
APP_DIR="$ROOT_DIR/django_pdf_view/"

parse_arguments "$@"

echo "Packaging django-pdf-view..."

if [ -d "$SRC_DIR" ]; then
  echo "Directory '$SRC_DIR' exists. Removing it..."
  rm -rf "$SRC_DIR"
fi

echo "Creating '$SRC_DIR' directory..."
mkdir -p "$SRC_DIR"

echo "Copying '$APP_DIR' app to '$SRC_DIR'..."
cp -r "$APP_DIR" "$SRC_DIR"

echo "Copying meta files into '$SRC_DIR'..."
cp "$META_DIR"* "$SRC_DIR"

echo "Building distribution files..."
python3 -m build "$SRC_DIR" --outdir "$DIST_DIR" || exit 1

echo "Checking distribution files..."
twine check "$DIST_DIR"* || exit 1

# Push to PyPI based on flags
if $PUSH_MAIN; then
  echo "Pushing to main PyPI..."
  twine upload "$DIST_DIR"* || exit 1
elif $PUSH_TEST; then
  echo "Pushing to test PyPI..."
  twine upload -r testpypi "$DIST_DIR"* || exit 1
else
  echo "No push option selected. Package built but not uploaded."
fi
