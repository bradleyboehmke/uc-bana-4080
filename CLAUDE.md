# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is UC BANA 4080: Introduction to Data Mining with Python - a course repository containing educational materials for teaching Python data science fundamentals. The repository includes:

- **Quarto book**: Course textbook content (Modules 1-6 plus appendices)
- **Jupyter notebooks**: Example notebooks, labs, and homework assignments  
- **Presentation slides**: Weekly lecture materials using Quarto/Reveal.js
- **Datasets**: CSV and Excel files for hands-on exercises
- **Python environment**: Configured with data science libraries

## Key Development Commands

### Building the Quarto Book
The main course textbook is built using Quarto:

```bash
# Navigate to book directory and render
cd book
quarto render

# Preview during development
quarto preview
```

### Creating Presentation Slides
Weekly slides use Quarto with Reveal.js format:

```bash
# From slides directory
cd slides
quarto render w[X]_[day].qmd  # e.g., w5_tuesday.qmd
quarto preview w[X]_[day].qmd
```

### Python Environment Setup
The course uses a Python virtual environment with specific data science packages:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Launch Jupyter for notebook development
jupyter lab
```

### Testing Jupyter Notebooks
All example notebooks and labs should be tested for functionality:

```bash
# Activate environment first
source venv/bin/activate

# Test individual notebook
jupyter nbconvert --to notebook --execute path/to/notebook.ipynb

# Clear outputs before committing
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace *.ipynb
```

## Repository Structure

### `/book/` - Course Textbook
- **Source files**: `.qmd` files for each chapter/module
- **Configuration**: `_quarto.yml` defines book structure and formatting
- **Built content**: `_book/` directory (auto-generated, git-tracked for GitHub Pages)
- **Assets**: `images/` directory with figures and screenshots

### `/slides/` - Weekly Presentations  
- **Lecture slides**: `w[X]_[day].qmd` format using Quarto + Reveal.js
- **Extensions**: Custom Quarto extensions for enhanced presentation features
- **Built slides**: `.html` files for web-based presentations

### `/example-notebooks/` - Course Examples
- **Numbered sequence**: `01_first_notebook.ipynb` through `17_functions.ipynb`
- **Companion script**: `my_first_script.py` for Python script demonstration
- **Purpose**: Step-by-step examples following textbook modules

### `/labs/` - Weekly Lab Activities
- **Lab sequence**: `01_python_intro.ipynb` through `05_wk5_lab.ipynb`  
- **Answer keys**: Some labs include `_answer_key.ipynb` versions
- **Interactive exercises**: Hands-on practice for students

### `/homework/` - Assignments
- **Student assignments**: `homework1.ipynb`, `homework2.ipynb`
- **Multiple formats**: Answer keys in `.ipynb`, `.html`, and `.pdf` formats
- **Grading support**: Complete solutions for instructor reference

### `/data/` - Course Datasets
- **CSV files**: Individual datasets like `airlines.csv`, `ames_clean.csv`
- **Excel files**: `products.xlsx` for spreadsheet import exercises  
- **Subdirectories**: `completejourney/` and `monthly_data/` for complex datasets
- **Real-world data**: Datasets chosen for practical data science applications

## Development Workflow

### Adding New Course Content
1. **Textbook chapters**: Create `.qmd` files in `/book/`, update `_quarto.yml` chapter list
2. **Example notebooks**: Follow naming convention, ensure outputs are cleared before commit
3. **Lab activities**: Create in `/labs/`, include both student and answer key versions
4. **Datasets**: Add to `/data/`, document structure and source in relevant notebooks

### Content Guidelines
- **Jupyter notebooks**: Always clear cell outputs before committing (except answer keys)
- **Google Colab integration**: Include Colab badges in notebook headers for student access
- **Progressive difficulty**: Content builds from Python basics through advanced data science topics
- **Real datasets**: Use authentic data to demonstrate practical applications

### Quality Assurance
- **Test all notebooks**: Ensure they run end-to-end in the specified environment
- **Quarto builds**: Verify book and slides render without errors
- **Link validation**: Check that internal references and external links work correctly
- **Accessibility**: Ensure content follows academic accessibility standards

## Course Modules Structure

The course follows a 6-module progression:

1. **Module 1**: Python fundamentals and environment setup
2. **Module 2**: Jupyter notebooks, data structures, libraries  
3. **Module 3**: Data importing, DataFrames, subsetting
4. **Module 4**: Data manipulation, aggregation, joins
5. **Module 5**: Data visualization with multiple libraries
6. **Module 6**: Control flow, iteration, functions

This structure should be preserved when adding or modifying content to maintain course coherence.