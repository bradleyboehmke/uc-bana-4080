# CLAUDE.md — BANA 4080 Development Guide

This file guides Claude Code when working in this repository.

## What this repo is

**BANA 4080: Introduction to Data Mining with Python** — a 14-week undergraduate
course at UC. Weeks 1–6 cover Python and data wrangling fundamentals, week 7 is
the midterm project, and weeks 8–14 cover machine learning.

- **Authoring layer:** Quarto (`.qmd` files) for textbook and slides
- **Lab format:** Jupyter notebooks (`.ipynb`)
- **Python stack:** pandas, numpy, matplotlib, seaborn, scikit-learn
- **Datasets:** CSV/Excel files in `data/`, plus the `completejourney_py` package
- **Deployment:** GitHub Actions renders the book and publishes to the `gh-pages`
  branch (`.github/workflows/publish-book.yml`). Slides are not yet published —
  Phase 9 of the migration moves the book to `docs/` and adds `docs/slides/` so
  module overview pages can link to the decks.

> **Migration in progress.** This repo is being restructured to match the layout
> and conventions of the sibling course repo at `../uc-bana-7025/`. See
> `MIGRATION-SPEC.md` for the phased plan. The layout below is the target
> structure; some directories may not exist yet.

## Repository layout

```
book/          Quarto textbook chapters (01–34 + index + appendices)
               NOTE: _quarto.yml currently lives inside book/. Phase 9 moves it
               (and index.qmd) to the repo root, matching 7025.
slides/        Weekly Reveal.js decks (week-01.qmd through week-14.qmd)
notebooks/     Jupyter notebooks (examples/)
labs/          Thursday lab assignments (.ipynb), plus ta-guides/
assignments/   homework/, midterm-project/, discussions/, quizzes/
instructor/    Instructor-only materials — NEVER expose to students
data/          Shared datasets
planning/      Course development materials (largely gitignored)
```

## Module → week mapping

| Module | Week | Chapters |
|--------|------|---------|
| 1 | 1 | 01-intro-data-mining, 02-preparing-for-code, 03-python-basics |
| 2 | 2 | 04-jupyter, 05-data-structures, 06-libraries |
| 3 | 3 | 07-importing-data, 08-dataframes, 09-subsetting |
| 4 | 4 | 10-manipulating-data, 11_aggregating_data, 12-joining-data |
| 5 | 5 | 13-data-viz-pandas, 14-advanced-data-viz, 15-exploratory-data-analysis |
| 6 | 6 | 16-control-statements, 17-iteration-statements, 18-functions |
| 7 | 7 | Midterm project (no textbook chapters, no lecture) |
| 8 | 8 | 19-intro-ml-ai, 20-before-we-build |
| 9 | 9 | 21-correlation-regression, 22-regression-evaluation |
| 10 | 10 | 23-logistic-regression, 24-classification-evaluation |
| 11 | 11 | 25-decision-trees, 26-random-forests, 27-feature-importance |
| 12 | 12 | 28-cross-validation, 29-hyperparameter-tuning, 30-feature-engineering |
| 13 | 13 | 31-clustering, 32-dimension-reduction |
| 14 | 14 | 33-modern-ml-algorithms, 34-ml-roadmap |

Module number and week number are always identical — Module N is Week N.

Modules 1–6 share their chapters with BANA 7025 — keep them in sync with
`../uc-bana-7025/book/`. Modules 7–14 are unique to BANA 4080. Module 7 is the
midterm project week: no chapters, no lecture, no cheatsheet, and Canvas holds the
authoritative project description and rubric.

## Content conventions

### Textbook chapters (`.qmd`)

- Start with a short intro paragraph (2–4 sentences), no preamble heading
- Second element: `By the end of this chapter, you will:` bullet list
- Use `##` for major sections, `###` for subsections
- Use Quarto callouts: `{.callout-note}`, `{.callout-tip}`, `{.callout-warning}`
- Python code blocks: ` ```python ` for non-executable, ` ```{python} ` for executable
- Use `#| eval: false` for code examples that shouldn't auto-run during render
- Include Colab badges pointing at `bradleyboehmke/uc-bana-4080`

### Slides (`.qmd` Reveal.js)

- YAML header includes `self-contained: true`, `slide-number: true`
- Title is the course name; subtitle is `"Week N: [Topic]"`; footer is `'BANA 4080 | Week N'`
- Use `{background="#2c3e50"}` for section divider slides
- Use `::: incremental` for bullet points that build
- Use `. . .` for pauses between blocks
- Keep each slide focused — one idea per slide

### Lab notebooks (`.ipynb`)

- Use markdown cells for setup, background, and instructions
- Structure: Overview → Setup → Problem sections → Reflection
- Clear all outputs before committing
- Include a ` ```python\n# Your code here\n``` ` placeholder for student work areas

## Python standards

- Prefer `pandas` method chaining over intermediate variables
- Use f-strings for string formatting
- Import style: `import pandas as pd`, `import numpy as np`, `import matplotlib.pyplot as plt`, `import seaborn as sns`
- DataFrames: snake_case names (e.g., `transactions`, `product_df`)
- scikit-learn: import estimators directly (`from sklearn.ensemble import RandomForestClassifier`);
  prefer `Pipeline` + `ColumnTransformer` over manual preprocessing steps

## Restricted content

- `instructor/` is always instructor-only
- Answer keys, solution notebooks, and quiz answers are never student-facing
- `planning/quizzes/` and `planning/gh-issues/` are gitignored — keep them that way

## Build commands

```bash
# Install Python dependencies
pip install -r requirements.txt

# Render the full book (run from book/, where _quarto.yml currently lives)
cd book && quarto render

# Live preview (recommended during authoring)
cd book && quarto preview

# Render a single chapter
cd book && quarto render 01-intro-data-mining.qmd

# Render or preview a slide deck
quarto render slides/week-01.qmd
quarto preview slides/week-01.qmd

# Clear Quarto cache
quarto clean
```

After Phase 9 the project moves to the repo root and these become:

```bash
quarto render          # book → docs/
quarto preview         # book only, no slides
bash render-slides.sh  # slides → docs/slides/
make all               # book + slides
```

## Adding new content

When adding a new chapter:
1. Create `book/NN-topic-name.qmd`
2. Add it to `book/_quarto.yml` under the correct module part
3. Run `quarto preview` from `book/` to verify it renders

When adding a new slide deck:
1. Create `slides/week-NN.qmd`
2. Use the existing `week-01.qmd` as a template

When adding a new lab:
1. Create `labs/lab-NN-topic.ipynb`
2. Follow the lab notebook conventions above
3. Place the answer key in `instructor/answer-keys/` (restricted)

## What NOT to do

- Do not commit Quarto cache or build output (`.quarto/`, `_book/`, `*_files/`)
- Do not commit notebook outputs — clear before committing (answer keys excepted)
- Do not commit instructor materials or answer keys to student-facing directories
- Do not generate content for graded assignments without explicit instruction
- Do not manually publish the book — let GitHub Actions deploy to `gh-pages`
