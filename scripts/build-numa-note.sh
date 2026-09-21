#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR/book"
latexmk -pdf -interaction=nonstopmode -halt-on-error numa-thin-zero-set-note.tex
mkdir -p "$ROOT_DIR/output/pdf"
cp numa-thin-zero-set-note.pdf "$ROOT_DIR/output/pdf/numa-thin-zero-set-note.pdf"
