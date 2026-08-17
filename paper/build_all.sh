#!/bin/bash
set -e
cd "$(dirname "$0")"
BIBTEX=$(command -v bibtex || true)
if [ -z "$BIBTEX" ] || [ ! -x "$BIBTEX" ]; then
  if [ -x /usr/bin/bibtex.original ]; then BIBTEX=/usr/bin/bibtex.original; fi
fi

build_one() {
  base="$1"
  rm -f "$base.aux" "$base.blg" "$base.log" "$base.out"
  pdflatex -interaction=nonstopmode "$base.tex"
  if [ -n "$BIBTEX" ]; then "$BIBTEX" "$base"; elif [ ! -s "$base.bbl" ]; then echo "BibTeX unavailable and $base.bbl missing" >&2; exit 127; fi
  pdflatex -interaction=nonstopmode "$base.tex"
  pdflatex -interaction=nonstopmode "$base.tex"
}

build_one main
build_one supplement
cp -f main.pdf fractional-memory-experiment-design.pdf
