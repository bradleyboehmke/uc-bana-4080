# BANA 4080 Migration Spec

Modernize BANA 4080 to match the structure and quality of the BANA 7025 repo at
`../uc-bana-7025/`. Weeks 1-7 content becomes identical to 7025 (same chapters,
same module overview format, same cheatsheets, same slide style). Weeks 8-13 adopt
the same structural patterns applied to the existing ML content.

Work through phases in order. Check in after each phase before proceeding.

---

## Module → Week mapping

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

Module number and week number are identical throughout — Module N is Week N.

---

## Phase 1: CLAUDE.md

Replace the current CLAUDE.md with one modeled after `../uc-bana-7025/CLAUDE.md`,
adapted for BANA 4080:

- Course name: BANA 4080: Introduction to Data Mining with Python
- 14-week course (weeks 1-6 Python fundamentals, week 7 midterm, weeks 8-14 ML)
- Use the module → week mapping table above
- Same content conventions, Python standards, and build commands as 7025
- Note that `book/_quarto.yml` lives inside `book/` (not repo root like 7025)
- Repo layout section should reflect the 4080 directory structure after migration:
  - `book/` — Quarto textbook chapters
  - `slides/` — Weekly Reveal.js decks (week-01.qmd through week-13.qmd)
  - `notebooks/examples/` — Companion example notebooks
  - `labs/` — Thursday lab assignments
  - `assignments/` — Homework, midterm-project, discussions, quizzes
  - `instructor/` — Instructor-only materials (never expose to students)
  - `data/` — Shared datasets

---

## Phase 2: Book chapters — shared with BANA 7025

Copy these files from `../uc-bana-7025/book/` into `book/` here, overwriting
the existing 4080 versions (which are older):

```
01-intro-data-mining.qmd
02-preparing-for-code.qmd
03-python-basics.qmd
04-jupyter.qmd
05-data-structures.qmd
06-libraries.qmd
07-importing-data.qmd
08-dataframes.qmd
09-subsetting.qmd
10-manipulating-data.qmd
11_aggregating_data.qmd
12-joining-data.qmd
13-data-viz-pandas.qmd
14-advanced-data-viz.qmd          ← replaces 14-data-viz-matplotlib.qmd
15-exploratory-data-analysis.qmd  ← replaces 15-data-viz-bokeh.qmd
16-control-statements.qmd
17-iteration-statements.qmd
18-functions.qmd
```

After copying:
- Delete `book/14-data-viz-matplotlib.qmd` and `book/15-data-viz-bokeh.qmd`
- Search-and-replace across all copied files: "BANA 7025" → "BANA 4080" and
  "uc-bana-7025" → "uc-bana-4080"
- Update any Colab badge URLs to point to `bradleyboehmke/uc-bana-4080`, and
  renumber the notebook they reference per the Phase 7 table (the copied 7025
  files carry 7025's offset numbering, which 4080 no longer uses)

The ML chapters (19-32) already exist in 4080 and are not touched in this phase.

---

## Phase 3: Module overview pages

**Modules 1-6**: copy from `../uc-bana-7025/book/`:
```
module-01-overview.qmd
module-02-overview.qmd
module-03-overview.qmd
module-04-overview.qmd
module-05-overview.qmd
module-06-overview.qmd
```

Adapt each file:
- "BANA 7025" → "BANA 4080", "uc-bana-7025" → "uc-bana-4080"
- Update slide links to the new filenames: `../slides/week-NN.html`
- Update Colab badge links to point to the correct 4080 notebooks under
  `notebooks/examples/` (see Phase 7 for final notebook names)
- Module 5 overview: reference ch14 (advanced-data-viz) and ch15
  (exploratory-data-analysis) — same as 7025 since we adopted those chapters

**Module 7 (midterm week)**: create `module-07-overview.qmd`. Keep it **high level**
— a short orientation to the Regork brief and what students will produce. Point to
**Canvas** for the official project description, deadlines, and grading rubric, and
treat Canvas as authoritative. This module has **no lecture**, so the Module
Resources section omits the Lecture table entirely (there is no week-07 slide deck).

**Modules 8-14**: create new overview files:
```
module-08-overview.qmd  (intro ML + ML workflow)
module-09-overview.qmd  (regression)
module-10-overview.qmd  (classification)
module-11-overview.qmd  (decision trees + random forests)
module-12-overview.qmd  (cross-validation, tuning, feature engineering)
module-13-overview.qmd  (clustering + dimension reduction)
module-14-overview.qmd  (modern ML algorithms + learning roadmap)
```

Module 14 is the final week of class — its framing should send students off with a
clear picture of where to continue their learning, so the overview should lean
forward (next topics, resources, career paths) rather than only summarizing.

Use the Module 1-6 overview files as the format template. Each should include:
- Module intro paragraph (2-4 sentences)
- `## Learning Objectives` with bullet list
- `## Module Resources` with tables for: Slides, Chapters & Notebooks, Lab, Reference (cheatsheet)

---

## Phase 4: Cheatsheets

**Modules 1-6**: copy from `../uc-bana-7025/book/`:
```
module-01-cheatsheet.qmd
module-02-cheatsheet.qmd
module-03-cheatsheet.qmd
module-04-cheatsheet.qmd
module-05-cheatsheet.qmd  ← covers seaborn + EDA (same as 7025 since we adopted those chapters)
module-06-cheatsheet.qmd
```

Adapt each: "BANA 7025" → "BANA 4080", update any repo URLs.

**Module 7** (midterm) gets **no cheatsheet** — its overview points students back at
the Module 1-6 cheatsheets, which cover everything the project needs.

**Modules 8-14**: create new cheatsheets covering the ML content for each module:
```
module-08-cheatsheet.qmd  (sklearn workflow, train/test split, pipelines)
module-09-cheatsheet.qmd  (LinearRegression, metrics, OLS interpretation)
module-10-cheatsheet.qmd  (LogisticRegression, classification metrics, ROC)
module-11-cheatsheet.qmd  (DecisionTreeClassifier, RandomForestClassifier, feature importance)
module-12-cheatsheet.qmd  (cross_val_score, GridSearchCV, preprocessing transformers)
module-13-cheatsheet.qmd  (KMeans, PCA, silhouette score)
module-14-cheatsheet.qmd  (gradient boosting, neural network basics, where to go next)
```

That is 13 cheatsheets total: modules 1-6 and 8-14.

Use the Module 1-6 cheatsheets as format templates. Focus on key sklearn API
patterns, common parameters, and example code snippets.

---

## Phase 5: Slides

This phase covers **filenames, YAML headers, and shared assets only**. Deck content
is deliberately left untouched — the 4080 decks are kept, not replaced with 7025's,
because they carry midterm project material 7025 has no equivalent for. Content
revision (interactivity, code-along notebooks, and the week 5 chapter mismatch) is
Phase 11.

### Rename files (in `slides/`)

| Old name | New name |
|----------|----------|
| `w1_tuesday_intro.qmd` | `week-01.qmd` |
| `w2_tuesday.qmd` | `week-02.qmd` |
| `w3_tuesday.qmd` | `week-03.qmd` |
| `w4_tuesday.qmd` | `week-04.qmd` |
| `w5_tuesday.qmd` | `week-05.qmd` |
| `w6_tuesday.qmd` | `week-06.qmd` |
| `w1_thursday_lab.qmd` | `week-01-lab.qmd` |
| `w2_thursday_lab.qmd` | `week-02-lab.qmd` |
| `w8_tuesday.qmd` | `week-08.qmd` |
| `w9_tuesday.qmd` | `week-09.qmd` |
| `w10_tuesday.qmd` | `week-10.qmd` |
| `w11_tuesday.qmd` | `week-11.qmd` |
| `w12_tuesday.qmd` | `week-12.qmd` |
| `w13_tuesday.qmd` | `week-13.qmd` |
| `w14_tuesday.qmd` | `week-14.qmd` (Module 13 — "Wrapping Up & Looking Forward") |
| `masters_extra_credit.qmd` | leave as-is |

Also rename the corresponding pre-built `.html` files to match (or delete them — they
will be regenerated on next `quarto render`).

**Do not create `week-07.qmd`.** Module 7 is the midterm project week and has no
lecture, so there is no week 7 deck. `render-slides.sh` globs `slides/week-*.qmd`,
so the gap is harmless.

### Update YAML headers

Update every slide file's YAML front matter to match this structure:

```yaml
---
title: "BANA 4080: Introduction to Data Mining with Python"
subtitle: "Week N: [Topic]"
format:
  revealjs:
    self-contained: true
    slide-number: true
    preview-links: auto
    revealjs-plugins:
      - appearance
      - highlight-text
    css:
      - styles.css
      - _extensions/martinomagnifico/appearance/appearance.css
    mermaid:
      theme: neutral
footer: 'BANA 4080 | Week N'
filters:
  - timer
---
```

### Copy shared slide assets from 7025

If any of these don't already exist in `slides/`, copy from `../uc-bana-7025/slides/`:
- `styles.css`
- `_metadata.yml`
- `_extensions/` directory (Quarto plugins for appearance/timer)

---

## Phase 6: Labs

Rename lab files in `labs/` to match 7025's `lab-NN-topic.ipynb` convention:

| Old name | New name |
|----------|----------|
| `01_python_intro.ipynb` | `lab-01-intro.ipynb` |
| `02_wk2_lab.ipynb` | `lab-02-data-structures.ipynb` |
| `03_wk3_lab.ipynb` | `lab-03-dataframes.ipynb` |
| `04_wk4_lab.ipynb` | `lab-04-manipulation.ipynb` |
| `04_wk4_lab_answer_key.ipynb` | move to `instructor/answer-keys/lab-04-answer-key.ipynb` |
| `05_wk5_lab.ipynb` | `lab-05-visualization.ipynb` |
| `06_midterm_project_template.ipynb` | move to `assignments/midterm-project/midterm-project.ipynb` |
| `08_wk8_lab.ipynb` | `lab-08-intro-ml.ipynb` |
| `09_wk9_lab.ipynb` | `lab-09-regression.ipynb` |
| `10_wk10_lab.ipynb` | `lab-10-classification.ipynb` |
| `11_wk11_lab.ipynb` | `lab-11-trees.ipynb` |
| `12_wk12_lab.ipynb` | `lab-12-model-tuning.ipynb` |
| `13_wk13_lab.ipynb` | `lab-13-clustering.ipynb` |
| `masters_extra_credit.ipynb` | leave as-is or move to `instructor/` |

Move all TA guidance notebooks into **`instructor/ta-guides/`** — not `labs/`. They
contain worked solutions, so they follow the same restricted-content pattern as
7025's `instructor/answer-keys/`: present on disk for instructors, gitignored so
they never reach the public repo.

```
ta_guidance_wk2.ipynb  → instructor/ta-guides/ta-guide-02.ipynb
ta_guidance_wk3.ipynb  → instructor/ta-guides/ta-guide-03.ipynb
ta_guidance_wk4.ipynb  → instructor/ta-guides/ta-guide-04.ipynb
ta_guidance_wk5.ipynb  → instructor/ta-guides/ta-guide-05.ipynb
ta_guidance_wk8.ipynb  → instructor/ta-guides/ta-guide-08.ipynb
ta_guidance_wk9.ipynb  → instructor/ta-guides/ta-guide-09.ipynb
ta_guidance_wk10.ipynb → instructor/ta-guides/ta-guide-10.ipynb
ta_guidance_wk12.ipynb → instructor/ta-guides/ta-guide-12.ipynb
```

`.gitignore` gains `instructor/ta-guides/`, `instructor/answer-keys/`, and
`instructor/planning/`, mirroring 7025.

`masters_extra_credit.ipynb` does not exist in this repo and is not being used —
no action needed.

---

## Phase 7: Example notebooks

Reorganize `example-notebooks/` to match 7025's `notebooks/examples/` structure:

1. Create `notebooks/` and `notebooks/examples/` directories
2. Move all notebooks from `example-notebooks/` into `notebooks/examples/`
3. Renumber the Python notebooks so each notebook's number matches the chapter it
   supports. Today they are offset by one (notebook `13_data_viz_matplotlib`
   supports chapter 14). **This is a deliberate divergence from BANA 7025**, which
   keeps the offset — 4080 chapters and notebooks will align, 7025's will not.

| Old name | New name | Chapter |
|----------|----------|---------|
| `01_first_notebook.ipynb` | `02_first_notebook.ipynb` | 02-preparing-for-code |
| `02_python_basics.ipynb` | `03_python_basics.ipynb` | 03-python-basics |
| `03_jupyter_notebook_basics.ipynb` | `04_jupyter_notebook_basics.ipynb` | 04-jupyter |
| `04_data_structures.ipynb` | `05_data_structures.ipynb` | 05-data-structures |
| `05_libraries.ipynb` | `06_libraries.ipynb` | 06-libraries |
| `06_importing_data.ipynb` | `07_importing_data.ipynb` | 07-importing-data |
| `07_dataframes.ipynb` | `08_dataframes.ipynb` | 08-dataframes |
| `08_subsetting.ipynb` | `09_subsetting.ipynb` | 09-subsetting |
| `09_manipulating_data.ipynb` | `10_manipulating_data.ipynb` | 10-manipulating-data |
| `10_aggregating_data.ipynb` | `11_aggregating_data.ipynb` | 11_aggregating_data |
| `11_relational_data.ipynb` | `12_relational_data.ipynb` | 12-joining-data |
| `12_data_viz_pandas.ipynb` | `13_data_viz_pandas.ipynb` | 13-data-viz-pandas |
| `13_data_viz_matplotlib.ipynb` | `14_advanced_data_viz.ipynb` | 14-advanced-data-viz |
| `14_data_viz_bokeh.ipynb` | `15_eda.ipynb` | 15-exploratory-data-analysis |
| `15_conditional_statements.ipynb` | `16_conditional_statements.ipynb` | 16-control-statements |
| `16_iteration_statements.ipynb` | `17_iteration_statements.ipynb` | 17-iteration-statements |
| `17_functions.ipynb` | `18_functions.ipynb` | 18-functions |

Only the numeric prefixes change; the topic slugs stay as they are (except the two
viz notebooks, whose topics genuinely changed). Chapter 01 has no notebook, and
chapters 19-20 have none either, so numbers 01 and 19-20 are simply unused.

Rename in **descending** order (17→18, then 16→17, …) so each rename doesn't
collide with the file already holding its target name.

The ML notebooks (21-32) are unique to 4080 and already align with their chapters —
keep their existing filenames:
```
21_correlation_regression.ipynb
22_regression_evaluation.ipynb
23_logistic_regression.ipynb
24_classification_evaluation.ipynb
25_decision_trees.ipynb
26_random_forests.ipynb
27_feature_importance.ipynb
28_cross_validation.ipynb
29_hyperparameter_tuning.ipynb
30_feature_engineering.ipynb
31_clustering.ipynb
32_dimension_reduction.ipynb
```

Also move these extra files from `example-notebooks/` appropriately:
- `my_first_script.py` → `notebooks/examples/my_first_script.py`
- `wk3_data_detective.ipynb`, `wk4_data_detective.ipynb` → `notebooks/examples/` (rename to `wk03_data_detective.ipynb`, `wk04_data_detective.ipynb`)
- `example_notebook.ipynb`, `example_homework_notebook.ipynb` → `notebooks/examples/`
- `tutorial_deep_learning_basics.ipynb` → `notebooks/examples/` (or `instructor/` if it's answer-key-level material)

Delete the now-empty `example-notebooks/` directory.

4. Update every Colab badge URL that points at a renumbered notebook. These live in
   the book chapters and the module overview pages (roughly 40 in chapters, 17 in
   overviews). Each URL needs three changes: the repo name, the
   `example-notebooks/` → `notebooks/examples/` path, and the new notebook number.
   Grep for `example-notebooks/` and `notebooks/examples/` under `book/` afterward
   to confirm none were missed.

Copy `../uc-bana-7025/notebooks/examples/README.md` into `notebooks/examples/README.md`
and update it to reflect 4080's notebook list (including the ML notebooks 21-32).

---

## Phase 8: Assignments

Create an `assignments/` directory structure matching 7025:

```
assignments/
  homework/
  midterm-project/
  discussions/
  quizzes/
```

**Homework**: move student-facing files from `homework/` into `assignments/homework/`:
```
homework1.ipynb → assignments/homework/homework-01.ipynb
homework2.ipynb → assignments/homework/homework-02.ipynb
```

**Answer keys — already done during Phase 6.** The keys that actually exist were
moved to `instructor/answer-keys/`, numbered by week (which equals the module):

```
homework_wk10_answer_key.{ipynb,html,pdf} → instructor/answer-keys/homework-10-answer-key.*
homework_wk11_answer_key.{ipynb,html,pdf} → instructor/answer-keys/homework-11-answer-key.*
homework_wk13_answer_key.{ipynb,pdf}      → instructor/answer-keys/homework-13-answer-key.*
```

The spec previously also listed keys for homework 1, 2, and week 9. Those files do
not exist in this repo. Remaining student-facing homework in `homework/`
(`homework_wk13.ipynb`, `homework_wk13_v2.*`, `wk12_homework.*`) is handled below.

**Midterm project**: the template was moved to `assignments/midterm-project/` in Phase 6.
Check `../uc-bana-7025/assignments/final-project/` for any additional scaffolding files
(rubrics, spec docs) to model a similar structure here.

**Discussions and quizzes**: create the directories. If there are quiz or discussion
files in `planning/` or elsewhere, move them here. Otherwise leave empty for now.

Delete the now-empty `homework/` directory.

---

## Phase 9: Build and publish pipeline

Adopt 7025's render/publish pipeline so the book and slides deploy together and
module overview pages can link students straight to the decks. Today 4080 renders
the book from inside `book/` and publishes only `book/` to `gh-pages`; slides are
never published, so `../slides/week-NN.html` links would 404.

**Run this phase after Phase 5**, since `render-slides.sh` globs `slides/week-*.qmd`.

### 9a. Move the Quarto project to the repo root

7025 keeps `_quarto.yml` and `index.qmd` at the root with `output-dir: docs` and
chapter paths prefixed `book/`. Mirror that:

1. `git mv book/_quarto.yml _quarto.yml`
2. `git mv book/index.qmd index.qmd`
3. `git mv book/references.bib references.bib` (if present at `book/`)
4. Add `output-dir: docs` under `project:`
5. Prefix every chapter/appendix path in the file with `book/`

Chapter bodies need **no** path edits: both repos already reference data as
`../data/foo.csv` and images as `images/foo.png` relative to the `.qmd` in `book/`,
and Quarto resolves those relative to the file, not the project root. Verified
identical across both repos.

### 9b. Book structure (`_quarto.yml` contents)

1. Use module overview pages as part headers — replace `part: "Module N"` strings with
   `part: book/module-NN-overview.qmd`
2. Update Module 5 chapters to list `14-advanced-data-viz.qmd` and
   `15-exploratory-data-analysis.qmd` (removing the old matplotlib/bokeh files)
3. List `module-07-overview.qmd` (the midterm) as a standalone entry, not a `part` —
   it has no chapters under it
4. Add a "Cheat Sheets" part at the end with all 13 module cheatsheets (1-6, 8-14)
5. Keep the existing ML chapter listings for Modules 8-14, updated with the new
   module overview files (Module 14 = 33-modern-ml-algorithms, 34-ml-roadmap)
6. Change the book title from "BANA 4080: Data Mining" to the full
   "BANA 4080: Introduction to Data Mining with Python"

**Do not copy 7025's `execute: eval: false`.** 7025 can disable execution because its
chapters carry pre-written output; 4080's ML chapters generate plots and model
results at render time (hence `book/31-clustering_files/figure-html/`). Leave 4080
executing.

### 9c. Slide rendering

1. Copy `../uc-bana-7025/render-slides.sh` to the repo root. It renders every
   `slides/week-*.qmd` and copies the HTML into `docs/slides/`.
2. Copy `../uc-bana-7025/Makefile` (`make preview` / `render` / `slides` / `all`),
   dropping the `uv run` prefix unless 4080 adopts uv.
3. Add `self-contained: true` to every deck in Phase 5 so the published HTML needs
   no sibling `_files/` directory.

With the book at `docs/` and slides at `docs/slides/`, the `../slides/week-NN.html`
links in the module overview pages resolve correctly from `docs/book/*.html`.

### 9d. GitHub Actions

Replace `.github/workflows/publish-book.yml` with 7025's version: render the book,
run `bash render-slides.sh`, then deploy `./docs` to `gh-pages` via
`peaceiris/actions-gh-pages@v4`. This replaces the current
`quarto-actions/publish` step that pushes only `book/`.

### 9e. Slide build output — already done in Phase 5

Phase 5 added `self-contained: true` to every deck, which inlines all assets and
pushes each rendered deck to roughly 10MB. That made committing them untenable, so
`slides/*.html` and `*_files/` were untracked and gitignored during Phase 5 rather
than here. Nothing to do in this step beyond confirming `render-slides.sh`
regenerates them into `docs/slides/`.

---

## Phase 10: Verify

1. Run `quarto render` from the repo root — verify the full book renders into `docs/`
   without errors, and that ML chapter figures still generate
2. Run `bash render-slides.sh` — verify every deck renders and lands in `docs/slides/`
3. Open `docs/book/module-01-overview.html` and follow its slide link — confirm
   `../slides/week-01.html` resolves against `docs/slides/`
4. Spot-check `slides/week-01.html` and `slides/week-08.html` for BANA 4080 branding
5. Check that all internal links resolve: module overview → slides, cheatsheets, Colab badges
6. Confirm Modules 8-14 overview pages link correctly to the ML labs and notebooks
7. Confirm the CI workflow's deploy step publishes `./docs`, not `book/`
8. Report any broken references or rendering errors

---

## Phase 11: Slide content revision (deferred)

Phase 5 renamed and restyled the decks but **did not touch their content**. This
phase revisits each deck the way the 7025 decks were revised: more interactive, with
a companion code-along notebook for each Tuesday lecture.

### Goals

- Work through `slides/week-01.qmd` … `week-14.qmd` one deck at a time
- Make them more interactive, following the pattern established in
  `../uc-bana-7025/slides/`
- Add a code-along notebook per Tuesday lecture (see below)

### Code-along notebooks

Mirror `../uc-bana-7025/notebooks/tuesday-your-turn/`, which holds student-facing
in-class notebooks that follow each lecture. Per that directory's README, each one
contains guided examples, short "Your Turn" exercises with `# Your code here`
placeholders, and brief reflection prompts.

Create `notebooks/tuesday-your-turn/` here with `week-NN-lecture.ipynb` for each
lecture week (1-6 and 8-14; module 7 is the midterm and has no lecture), plus a
README.

Once these exist, restore the "Tuesday Your Turn Notebook" row in the affected
module overview pages. Phase 3 dropped that row for modules 2, 5, and 6 because
4080 had no equivalent, and pointed modules 3 and 4 at the existing
`wk03_data_detective` / `wk04_data_detective` notebooks instead. Modules 8-14 never
had the row.

### Known content gap to fix first

**Week 5 does not match its chapters.** Phase 2 replaced the old matplotlib and
Bokeh chapters with `14-advanced-data-viz` (Seaborn-led) and
`15-exploratory-data-analysis`, but the week 5 deck still reflects the old
chapters — Matplotlib is mentioned 17 times and Bokeh 14, against 2 for Seaborn and
1 for EDA. 7025's week 5 deck is weighted to match the new chapters (Seaborn 20,
Matplotlib 26, Bokeh 9, plus EDA).

Recommended fix is a merge rather than a copy: bring 7025's Seaborn and EDA material
into the 4080 deck, reduce the Bokeh coverage to match the chapter's lighter
treatment, and **keep the existing 4080 Mid-term section**.

### What not to lose

The 4080 decks carry midterm project material that 7025 has no equivalent for —
7025 runs a semester-long project with weekly checkpoints instead. Preserve it when
revising:

- `week-05.qmd` — "Mid-term" section: deadline countdown, the Thursday lab dedicated
  to project work, pointer to the rubric
- `week-06.qmd` — "Mid-term Project Discussion" section: Canvas groups, timeline,
  requirements, logistics
- `week-01.qmd` — brief midterm references

Weeks 1-4 and 6 still match their chapters on content, so they need interactivity
work but no correction.
