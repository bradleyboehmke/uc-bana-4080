# Example Notebooks

Companion notebooks for the BANA 4080 textbook. Each one contains the runnable code
from its chapter — open it in Colab from the chapter's badge, or clone the repo and
run it locally.

**Notebook numbers match chapter numbers.** Notebook `08_dataframes.ipynb` accompanies
Chapter 8. Chapters 1, 19, 20 and 34 are discussion chapters with no companion
notebook, so those numbers are unused.

## Python foundations (Modules 1–6)

| Notebook | Chapter | Topic |
|----------|---------|-------|
| `02_first_notebook.ipynb` | 2 | Preparing for code |
| `03_python_basics.ipynb` | 3 | Python basics |
| `04_jupyter_notebook_basics.ipynb` | 4 | Jupyter notebooks |
| `05_data_structures.ipynb` | 5 | Data structures |
| `06_libraries.ipynb` | 6 | Packages and libraries |
| `07_importing_data.ipynb` | 7 | Importing data |
| `08_dataframes.ipynb` | 8 | DataFrames |
| `09_subsetting.ipynb` | 9 | Subsetting data |
| `10_manipulating_data.ipynb` | 10 | Manipulating data |
| `11_aggregating_data.ipynb` | 11 | Aggregating data |
| `12_relational_data.ipynb` | 12 | Joining data |
| `13_data_viz_pandas.ipynb` | 13 | Visualization with Pandas |
| `14_advanced_data_viz.ipynb` | 14 | Seaborn, Matplotlib, Bokeh |
| `15_eda.ipynb` | 15 | Exploratory data analysis |
| `16_conditional_statements.ipynb` | 16 | Control statements |
| `17_iteration_statements.ipynb` | 17 | Iteration statements |
| `18_functions.ipynb` | 18 | Writing functions |

## Machine learning (Modules 8–14)

| Notebook | Chapter | Topic |
|----------|---------|-------|
| `21_correlation_regression.ipynb` | 21 | Correlation and linear regression |
| `22_regression_evaluation.ipynb` | 22 | Evaluating regression models |
| `23_logistic_regression.ipynb` | 23 | Logistic regression |
| `24_classification_evaluation.ipynb` | 24 | Evaluating classification models |
| `25_decision_trees.ipynb` | 25 | Decision trees |
| `26_random_forests.ipynb` | 26 | Random forests |
| `27_feature_importance.ipynb` | 27 | Feature importance |
| `28_cross_validation.ipynb` | 28 | Cross-validation |
| `29_hyperparameter_tuning.ipynb` | 29 | Hyperparameter tuning |
| `30_feature_engineering.ipynb` | 30 | Feature engineering |
| `31_clustering.ipynb` | 31 | Clustering |
| `32_dimension_reduction.ipynb` | 32 | Dimension reduction with PCA |
| `tutorial_deep_learning_basics.ipynb` | 33 | Deep learning basics |

## In-class and reference notebooks

| File | Purpose |
|------|---------|
| `wk03_data_detective.ipynb` | Week 3 in-class follow-along |
| `wk04_data_detective.ipynb` | Week 4 in-class follow-along |
| `example_notebook.ipynb` | Formatting reference for notebook submissions |
| `example_homework_notebook.ipynb` | Formatting reference for homework |
| `my_first_script.py` | Companion Python script for Chapter 2 |

## Running these

Most notebooks load data straight from a URL, so they run anywhere. A few read from
`../../data/` instead — keep the repo structure intact when running those locally.
In Colab, the badge handles everything for you.

```bash
pip install -r requirements.txt
jupyter lab
```
