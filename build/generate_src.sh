#!/bin/bash

BUILD_SCRIPT_PATH=$(realpath "$0")
BUILD_DIR=$(dirname "$BUILD_SCRIPT_PATH")
ROOT_DIR=$(dirname "$BUILD_DIR")

SRC_DIR="$BUILD_DIR/src"

echo "Preparing source files..."

if [ -d "$SRC_DIR" ]; then
    echo "\tDirectory 'src' exists. Removing it..."
    rm -rf "$SRC_DIR"
fi

echo "\tCreating 'src' directory..."
mkdir -p "$SRC_DIR"

echo "\tCopying 'django_pdf' app to 'src'..."
cp -r "$ROOT_DIR/django_pdf" "$SRC_DIR"

echo "\tCopying meta files into 'src'..."
cp "$BUILD_DIR/assets/"* "$SRC_DIR"

echo "Finished preparing source files."
