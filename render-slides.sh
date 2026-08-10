#!/bin/bash
# Render all slide decks to docs/slides/
# Run after `quarto render` so docs/ already exists.

set -e
mkdir -p docs/slides

for f in slides/week-*.qmd; do
  echo "Rendering $f..."
  quarto render "$f"
done

cp slides/week-*.html docs/slides/
echo "Slides copied to docs/slides/"
