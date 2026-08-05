#!/bin/bash
set -e  # Exit on any error

cd "$(dirname "$0")"

echo "Running pdflatex..."
pdflatex -interaction=nonstopmode main.tex
echo "Running bibtex..."
bibtex main.aux
echo "Running pdflatex again..."
pdflatex -interaction=nonstopmode main.tex
echo "Running pdflatex final time..."
pdflatex -interaction=nonstopmode main.tex

echo "Build complete. Output PDF: main.pdf"
