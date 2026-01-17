#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "latexmk not found; skipping PDF build."
  exit 0
fi

python3 "$root_dir/scripts/render_tex.py"

mkdir -p "$root_dir/assets"

if [[ -f "$root_dir/tex/out/cv.tex" ]]; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
    -output-directory="$root_dir/tex/out" "$root_dir/tex/out/cv.tex"
  cp "$root_dir/tex/out/cv.pdf" "$root_dir/assets/cv.pdf"
else
  echo "Missing tex/out/cv.tex; skipping CV PDF build."
fi

if [[ -f "$root_dir/tex/out/publications.tex" ]]; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
    -output-directory="$root_dir/tex/out" "$root_dir/tex/out/publications.tex"
  cp "$root_dir/tex/out/publications.pdf" "$root_dir/assets/publications.pdf"
else
  echo "Missing tex/out/publications.tex; skipping Publications PDF build."
fi
