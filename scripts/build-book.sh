#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT_DIR/scripts/check-citation-placement.py"
cd "$ROOT_DIR/book"
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
mkdir -p "$ROOT_DIR/output/pdf"
cp book.pdf "$ROOT_DIR/output/pdf/hermitian-pluripotential-theory.pdf"
