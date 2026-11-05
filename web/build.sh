#!/usr/bin/env bash
# Build the GitHub Pages site into site/.
# web/prepare_docs.py copies the notes into docs/ (the Obsidian folders stay
# untouched) and converts wikilinks; then MkDocs builds the site.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf docs site
python web/prepare_docs.py
mkdocs build --strict
