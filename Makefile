.PHONY: preview render slides all clean

# Fast: preview book only (no slides)
preview:
	quarto preview

# Book only (no slides)
render:
	quarto render

# Slides only
slides:
	@mkdir -p docs/slides
	@for f in slides/week-*.qmd; do \
		echo "Rendering $$f..."; \
		quarto render "$$f"; \
	done
	@cp slides/week-*.html docs/slides/
	@echo "Slides copied to docs/slides/"

# Full production build: book + slides
all: render slides

clean:
	quarto clean
