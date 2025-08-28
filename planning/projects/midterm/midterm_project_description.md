# Mid-Term Project: Regork Grocery Chain Analytics

## Scenario

You are a data scientist for a national grocery chain named **Regork**. Your manager has asked you to identify a potential growth opportunity where the company could invest future resources to increase revenue and profits.

Your task is to:

1. Define a clear business question that investigates a specific growth opportunity
2. Analyze the company's data to answer that question
3. Communicate your findings through:
   - A written analytic report (produced in Jupyter Notebook and shared as HTML)
   - A 3-minute business presentation to the CEO

This project simulates a real-world analytics engagement where the problem statement may be broad at first, and it's your job to refine it, find meaningful insights, and make actionable recommendations.

## Business Question

Growth opportunities can take many forms. Your first task is to propose and refine a business question that focuses your analysis. You will use data to defend your proposition and support a clear recommendation.

Here are some example questions to inspire your thinking:

### Customer segments & demographics
- Are certain demographic groups underrepresented in specific product categories?
- Are there untapped demographics for certain products due to lack of marketing?

### Trends over time
- Do purchasing patterns shift seasonally or around holidays?
- Are certain products or customer segments showing sales growth or decline?

### Product relationships
- Are certain products frequently purchased together?
- Example: Are frozen pizzas and beer often bought in the same transaction?

### Promotions & marketing
- Which promotions drive the most revenue uplift?
- Are certain campaigns more successful for specific products or customer groups?

**Important:** Your business question may evolve as you explore the data, but your final report must clearly state one main question and fully address it.

## Analytic Approach

Once you have a business question, design a clear and logical plan to answer it.

A strong analysis should:

- Tell a clear narrative that ties your findings back to the business question
- Use appropriate visuals that enhance the story (not just charts for the sake of charts)
- End with specific, actionable recommendations—tell the CEO exactly what to do next

### Example:

**Business Question:** Are frozen pizzas and beer commonly purchased together?

**Approach:** Join transactions + products, identify relevant items, compute co-purchase rates, visualize results.

**Dig Deeper:**
- Is the co-purchase more common Thursday–Saturday than earlier in the week?
- Does it spike during football season compared to the rest of the year?
- Are these items co-purchased more by households with kids than those without?

**Refined Recommendation:** Based on these findings, run targeted "Pizza & Beer" promotions Thursday–Saturday, especially during football season, and focus marketing toward households with kids.

**Bottom line:** Provide a robust, multi-angle understanding of the business problem so you can paint a complete picture for the CEO.

## Data

You will use the **completejourney** dataset via the Python `completejourney_py` package.

- **Full dataset documentation:** [completejourney R package site](https://bradleyboehmke.github.io/completejourney/)
- **You must use at least two datasets** from the package and join them in a meaningful way
- Your analysis should demonstrate thoughtful data selection, joining, and preparation to address your business question

## Deliverables

### A. Written Report

**Format:** HTML report generated from a Jupyter Notebook

**Content Requirements:**
- Import, assess, clean, and prepare the data
- Clearly state your business question
- Perform EDA and/or modeling (modeling is optional)
- Present findings as a cohesive narrative, not just a set of statistics or charts
- **Code Display:** Show all relevant code, but hide unnecessary warnings, errors, or distracting output
- **Formatting:** Follow the report formatting requirements in the grading rubric

**File Naming:** Use the format `YYYY_BANA4080_groupXX_finalproject.html`
- Example: `2025_BANA4080_group02_finalproject.html`

### B. Presentation

**Length:** 3 minutes (maximum)

**Audience:** Senior business executive (CEO)

**Content:**
- State the business problem
- Summarize key findings
- Provide a clear, actionable recommendation

**Format:**
- No code — this is a business presentation
- Use visuals and language appropriate for an executive audience

## Past Examples

Here are a few submissions from a similar class that provide examples of good quality submissions:

- [Targeting parents vs. non-parent Customers](example-links)
- [More efficient campaigns](example-links)
- [Improving pizza sales](example-links)
- [Display location performance](example-links)

## Groups

- Work in teams of **2–4 students**
- You may self-select your team from the pre-defined groups listed in Canvas (People → Mid-Term Project)
- **You must join one of the listed groups**
- **You may not create your own group** outside of the list

### Peer Evaluations:
- You will evaluate your teammates' contributions at the end of the project
- Peer evaluations count toward **25% of your engagement grade**
- Unequal contributions will affect individual grades

## Submission Guidelines

- **One group member submits** all final files on behalf of the team
- Submit **both deliverables together** (HTML report and presentation video) in a single submission
- If multiple members submit, only the most recent submission will be kept for all group members
- Submitting files separately may result in one file overwriting the other

### Plan ahead:
- Large files (e.g., a 4–5 MB presentation video) may take time to upload
- Submit several hours before the deadline to avoid last-minute technical issues
- **Late submissions due to upload delays will not be excused**

## Grading

Your project will be graded by both the instructor and your peers using the posted rubric.

**Review the rubric carefully** before starting to ensure your work meets all expectations.

### Peer Review Requirement:
- You must complete peer reviews for **1 or more other teams** (both report and presentation)
- **Failure to submit your peer reviews will result in a 25% deduction** from your engagement grade
- To complete a peer review, follow the provided instructions and fill out the grading rubric

## Presentation Tools & Resources

### Recommended Recording Tools:
- **Zoom** – Start a meeting, share your slides, click record, and present
- **Kaltura** – Upload and share your presentation video in Canvas

### Help & Tutorials:
- UC Zoom Information
- Kaltura Upload Tutorial

---

**Points:** 75