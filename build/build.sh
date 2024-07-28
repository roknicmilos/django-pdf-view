#!/bin/bash

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
    exit 1
}

# Initialize flags:
PUSH_MAIN=false
PUSH_TEST=false

# Parse the first command-line argument if provided:
if [ "$1" ]; then
    if [ "$1" = "--push-main" ]; then
        PUSH_MAIN=true
    elif [ "$1" = "--push-test" ]; then
        PUSH_TEST=true
    elif [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
        show_usage
    else
        echo "Unknown command: '$1'"
        show_usage
        exit 1
    fi
fi

# Initialize directory path variables:
BUILD_SCRIPT_PATH=$(realpath "$0")
BUILD_DIR=$(dirname "$BUILD_SCRIPT_PATH")
ROOT_DIR=$(dirname "$BUILD_DIR")
SRC_DIR="$BUILD_DIR/src"

########################################################
############# Main script execution ####################
########################################################
echo "Packaging django-pdf-view..."

if [ -d "$SRC_DIR" ]; then
    echo "Directory 'src' exists. Removing it..."
    rm -rf "$SRC_DIR"
fi

echo "Creating 'src' directory..."
mkdir -p "$SRC_DIR"

echo "Copying 'django_pdf_view' app to 'src'..."
cp -r "$ROOT_DIR/django_pdf_view" "$SRC_DIR"

echo "Copying meta files into 'src'..."
cp "$BUILD_DIR/meta/"* "$SRC_DIR"

echo "Building distribution files..."
python3 -m build "$SRC_DIR" || exit 1

echo "Checking distribution files..."
twine check "$SRC_DIR/dist/"* || exit 1

# Push to PyPI based on flags
if $PUSH_MAIN; then
    echo "Pushing to main PyPI..."
    twine upload "$SRC_DIR/dist/"* || exit 1
elif $PUSH_TEST; then
    echo "Pushing to test PyPI..."
    twine upload -r testpypi "$SRC_DIR/dist/"* || exit 1
else
    echo "No push option selected. Package built but not uploaded."
fi
