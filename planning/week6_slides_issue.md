# Create Week 6 Tuesday Slides: Control Flow, Iteration, and Functions

## Overview
Create presentation slides for Week 6 Tuesday class introducing students to writing efficient Python code through control statements, iteration, and functions. This class prepares students for Thursday's hands-on lab session.

**Target Duration:** 60-75 minutes  
**Audience:** Business analytics undergrads (juniors/seniors) new to Python programming

## Slide Structure Requirements

### 1. Week 5 Review & Pop Quiz (15-20 minutes)
- **Quick review** of data visualization concepts from Week 5
- **Business-focused pop quiz** that requires applying Week 5 visualization knowledge:
  - Present real business scenarios where students must think about:
    - Which chart type to choose for specific business questions
    - How to interpret visualizations for business insights
    - When to use pandas plotting vs matplotlib vs bokeh
  - **Example scenarios:**
    - "Your manager wants to see monthly sales trends across regions - what visualization approach would you recommend and why?"
    - "You need to present customer segmentation results to executives - how would you visualize cluster analysis results?"
    - "A stakeholder asks about the relationship between marketing spend and revenue - what would you create?"

### 2. Week 6 Content Introduction (35-45 minutes)

#### 2a. Control Statements (12-15 minutes)
**Key concepts from `book/16-control-statements.qmd`:**
- When programs need to "make decisions"
- Basic `if/elif/else` syntax and business logic
- **Business examples:**
  - Customer segmentation (high/medium/low value)
  - Discount eligibility rules
  - Inventory restocking decisions
- Dictionary-based switch statements for business rules
- Vectorized conditionals in pandas for large datasets

#### 2b. Iteration Statements (12-15 minutes) 
**Key concepts from `book/17-iteration-statements.qmd`:**
- Automating repetitive business tasks
- `for` loops for processing multiple files/datasets
- `while` loops for conditional processing
- **Business examples:**
  - Processing monthly sales reports
  - Calculating metrics across store locations
  - Automating data quality checks
- List comprehensions for efficient data transformations
- When to use loops vs pandas vectorized operations

#### 2c. Functions (10-15 minutes)
**Key concepts from `book/18-functions.qmd`:**
- Why business analysts need reusable code
- DRY principle (Don't Repeat Yourself) in business context
- **Business examples:**
  - Creating reusable calculation functions (ROI, profit margins)
  - Building data cleaning pipelines
  - Custom business metrics functions
- Function documentation for team collaboration
- Brief introduction to lambda functions for data transformations

### 3. Mid-term Project Discussion (10-15 minutes)
- **Project overview and expectations**
- **Timeline and milestones**
- **Team formation** (if applicable)
- **Dataset options** and business problem selection
- **Q&A session** for project clarification
- **Resource sharing** (where to get help, office hours, etc.)

## Deliverables

### Required Files:
- [ ] `slides/w6_tuesday.qmd` - Main presentation file
- [ ] Update any necessary images in `slides/images/`
- [ ] Rendered HTML version: `slides/w6_tuesday.html`

### Presentation Requirements:
- [ ] **Conceptual focus** - minimal live coding, more theory and examples
- [ ] **Business context** throughout - relate all concepts to business analytics use cases  
- [ ] **Interactive elements** - polls, discussion questions, pop quiz
- [ ] **Visual examples** - code snippets that illustrate concepts clearly
- [ ] **Clear learning objectives** stated at beginning
- [ ] **Transition statements** connecting to Thursday's lab work

### Pop Quiz Specifications:
- [ ] **3-5 questions** that require applying Week 5 visualization concepts
- [ ] **Real business scenarios** (not abstract coding problems)
- [ ] **Multiple choice or short discussion format** for quick feedback
- [ ] **Explanations provided** for learning reinforcement

## Technical Specifications

### Slide Format:
- Use existing Quarto reveal.js template from previous weeks
- Include timer extension for pacing
- Maintain consistent styling with course branding
- Ensure mobile-friendly for students following along

### Code Examples:
- **Minimal but illustrative** - focus on concept clarity
- **Business data contexts** - use retail, sales, customer data examples
- **Progressive complexity** - start simple, build to more realistic scenarios
- **Error-free and tested** - all code should run without issues

## Success Criteria
- [ ] Students can explain when to use conditional statements in business contexts
- [ ] Students understand the value of automation through loops and functions
- [ ] Students can identify business scenarios where each concept applies
- [ ] Students are prepared for hands-on Thursday lab exercises
- [ ] Mid-term project expectations are clearly communicated
- [ ] Presentation stays within 75-minute time limit

## Additional Notes
- **Coordinate with Thursday lab** - ensure concepts introduced here are practiced in lab
- **Student engagement** - include discussion prompts throughout
- **Real-world relevance** - emphasize how these skills improve their future careers
- **AI tool integration** - mention how ChatGPT/Copilot can help with coding
- **Preparation for advanced topics** - hint at machine learning applications coming later

## Resources
- Reference textbook chapters: 16-control-statements.qmd, 17-iteration-statements.qmd, 18-functions.qmd
- Example notebooks: `example-notebooks/15_conditional_statements.ipynb`, `16_iteration_statements.ipynb`, `17_functions.ipynb`
- Previous week slides for format consistency
- Business datasets from `data/` folder for relevant examples