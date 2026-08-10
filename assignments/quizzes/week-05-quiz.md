# Week 5 Reading Quiz

**Module:** 5 — Data Visualization & EDA  
**Chapters:** 13 (Visualization with Pandas), 14 (Advanced Data Visualization), 15 (Exploratory Data Analysis)  
**Points:** 14 (1 pt per question)  
**Time limit:** 40 minutes  
**Attempts:** Up to 2 — final score is the average of both attempts

> Questions focus on conceptual knowledge and high-level comprehension rather
> than coding. If you don't feel confident after the first try, review the lesson
> materials and try again.

---

**Question 1** — *Multiple Choice*

What is the primary difference between **exploratory** and **explanatory** visualization?

- Exploratory charts use Seaborn; explanatory charts use Matplotlib
- Exploratory charts are made for the analyst during analysis; explanatory charts are polished for communicating findings to an audience
- Exploratory charts are interactive; explanatory charts are static
- Exploratory charts show distributions; explanatory charts show relationships

---

**Question 2** — *Multiple Choice*

Pandas `.plot()` is described in the chapter as a "wrapper" around another library. Which library does it wrap?

- Seaborn
- Bokeh
- Matplotlib
- Plotly

---

**Question 3** — *Multiple Choice*

When using Pandas `.plot()`, which of the following is required when creating a **two-variable** plot (e.g., a scatter plot) but NOT a **one-variable** plot (e.g., a histogram)?

- `figsize=`
- `title=`
- `x=` and `y=`
- `kind=`

---

**Question 4** — *True/False*

When working with time series data, `.resample()` is preferred over `.groupby()` because it understands date and time frequencies (e.g., `'D'` for daily, `'W'` for weekly).

- True
- False

---

**Question 5** — *Multiple Choice*

You want to compare the spread of basket spend across income brackets and identify outliers. Which chart type is best suited for this?

- Line chart
- Histogram
- Box plot
- Bar chart

---

**Question 6** — *Multiple Choice*

According to the chapter, which Python visualization library is best suited for creating **interactive, web-ready charts** that let viewers zoom, pan, and hover over data points?

- Seaborn
- Matplotlib
- Pandas
- Bokeh

---

**Question 7** — *Multiple Choice*

In Matplotlib's Figure/Axes model, what does the `ax` object represent?

- The full output file including title and figure size
- The actual plot area where data, axes, labels, and ticks are drawn
- The color palette applied to the chart
- The data source connected to the chart

---

**Question 8** — *True/False*

Seaborn is an independent visualization library that has no relationship to Matplotlib — charts created with Seaborn cannot be further customized using Matplotlib methods.

- True
- False

---

**Question 9** — *Multiple Select*

Which of the following are advantages of Bokeh over Matplotlib?

*(Select all that apply)*

- Users can zoom, pan, and hover without writing new code
- Charts render as self-contained HTML that can be shared without Python
- It requires less code than Seaborn for statistical group comparisons
- Hover tooltips can display formatted values tied to specific data points

---

**Question 10** — *Multiple Choice*

In a Seaborn function call, what does the `hue=` parameter do?

- Sets the color of the plot background
- Adds a color dimension by grouping data according to a categorical column
- Controls the transparency of plotted points
- Specifies the column to use for the y-axis

---

**Question 11** — *Multiple Choice*

According to the EDA framework in Chapter 15, what is the correct order of steps?

- Distributions → Structure → Question → Segmentation → Story
- Question → Structure → Distributions → Segmentation → Story
- Structure → Question → Segmentation → Distributions → Story
- Story → Question → Distributions → Structure → Segmentation

---

**Question 12** — *True/False*

Exploratory Data Analysis (EDA) is best described as a fixed checklist of charts and summary statistics that every analyst should run in the same order.

- True
- False

---

**Question 13** — *Multiple Choice*

In a right-skewed distribution, which of the following is true?

- The mean and median are approximately equal
- The mean is less than the median
- The mean is greater than the median
- The distribution has no outliers

---

**Question 14** — *Multiple Select*

Which of the following are characteristics of a **sharp** business question that makes it suitable for EDA?

*(Select all that apply)*

- It names a specific unit of analysis (e.g., basket, household, store)
- It specifies a metric to measure (e.g., spend, frequency, redemption rate)
- It includes a comparison or segmentation to make
- It is broad enough to avoid restricting what the data might reveal
- You would know when you had answered it
