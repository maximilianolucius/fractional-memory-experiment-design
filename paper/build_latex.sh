#!/bin/bash
set -e
cd "$(dirname "$0")"

echo "Running pdflatex..."
pdflatex -interaction=nonstopmode main.tex

if command -v bibtex >/dev/null 2>&1; then
  echo "Running bibtex..."
  bibtex main.aux
else
  if [ ! -s main.bbl ]; then
    echo "ERROR: bibtex is unavailable and main.bbl is missing/empty." >&2
    exit 127
  fi
  echo "bibtex not found; reusing released main.bbl."
fi

echo "Running pdflatex again..."
pdflatex -interaction=nonstopmode main.tex
echo "Running pdflatex final time..."
pdflatex -interaction=nonstopmode main.tex
if grep -q 'Label(s) may have changed' main.log; then
  echo "Labels changed; one more pdflatex pass..."
  pdflatex -interaction=nonstopmode main.tex
fi

echo "Producing final PDF name..."
cp -f main.pdf fractional-memory-experiment-design.pdf

echo "Build complete. Output PDF: fractional-memory-experiment-design.pdf (main.pdf kept as build artifact)"
