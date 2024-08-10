#!/bin/sh

run_checks() {
  # Check if a version argument is provided
  if [ -z "$1" ]; then
    echo "Usage: $0 <version>"
    exit 1
  fi

  # Check if the current branch is 'main'
  CURRENT_BRANCH=$(git branch --show-current)
  if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "Error: You are not on the 'main' branch. Current branch is '$CURRENT_BRANCH'."
    exit 1
  fi

  # Check if the 'main' branch is up to date
  git fetch origin main

  LOCAL_COMMIT=$(git rev-parse main)
  REMOTE_COMMIT=$(git rev-parse origin/main)

  if [ "$LOCAL_COMMIT" != "$REMOTE_COMMIT" ]; then
    echo "Error: The 'main' branch is not up to date with 'origin/main'."
    exit 1
  fi
}

################################################################
################# Main script execution ########################
################################################################
run_checks "$@"

# Initialize variables
VERSION=$1
THIS_SCRIPT=$(realpath "$0")
SCRIPTS_DIR=$(dirname "$THIS_SCRIPT")
ROOT_DIR=$(dirname "$SCRIPTS_DIR")
META_DIR="$ROOT_DIR/meta/"
PYPROJECT_FILE="$META_DIR/pyproject.toml"
BUILD_SCRIPT="$SCRIPTS_DIR/build.sh"

# Update the version in pyproject.yaml
sed -i "s/^version = \".*\"/version = \"$VERSION\"/" "$PYPROJECT_FILE"

# Commit the change
git add pyproject.toml
git commit -m "Update package version to $VERSION"

# Create a git tag
git tag "v$VERSION"

# Push the commit and the tag
git push origin main
git push origin "v$VERSION"

# Build the distribution files and push to PyPI
sh "$BUILD_SCRIPT" --push-main
