# Week 4 Reading Quiz

**Module:** 4 — Data Manipulation  
**Chapters:** 10 (Manipulating Data), 11 (Aggregating Data), 12 (Joining Data)  
**Points:** 11 (1 pt per question)  
**Time limit:** 40 minutes  
**Attempts:** Up to 2 — final score is the average of both attempts

> Questions focus on conceptual knowledge and high-level comprehension rather
> than coding. If you don't feel confident after the first try, review the lesson
> materials and try again.

---

**Question 1** — *Multiple Choice*

When using Pandas, which method allows you to rename columns in a DataFrame by providing a dictionary mapping old names to new names?

- `DataFrame.rename()`
- `DataFrame.rename_columns()`
- `DataFrame.set_columns()`
- `DataFrame.columns.rename()`

---

**Question 2** — *Multiple Choice*

If you want to permanently rename a column in a DataFrame without having to reassign the DataFrame to a new variable, which argument must you include in `rename()`?

- `permanent=True`
- `inplace=True`
- `overwrite=True`
- `persist=True`

---

**Question 3** — *Multiple Choice*

Which method removes one or more columns from a DataFrame?

- `drop()`
- `remove()`
- `delete_columns()`
- `remove_columns()`

---

**Question 4** — *Multiple Choice*

When calling `drop()` to remove a column, which parameter do you set to indicate you're removing columns instead of rows?

- `axis=0`
- `axis=1`
- `columns=True`
- `direction="columns"`

---

**Question 5** — *Multiple Choice*

Which method is best for detecting missing values in a DataFrame?

- `isna()` or `isnull()`
- `missing()`
- `nullcheck()`
- `checkna()`

---

**Question 6** — *Multiple Choice*

If you want to replace all missing values in a column with the mean of that column, which method should you use?

- `fillna()`
- `replace()`
- `impute()`
- `meanfill()`

---

**Question 7** — *Multiple Choice*

Which Pandas function allows you to compute summary statistics for all columns in a DataFrame **at once**?

- `summary()`
- `describe()`
- `info()`
- `aggregate()`

---

**Question 8** — *Multiple Choice*

What is the main purpose of `groupby()` in Pandas?

- To split the DataFrame into subsets based on one or more keys and apply aggregations
- To sort the DataFrame alphabetically by column names
- To combine multiple DataFrames together
- To filter out missing values from a DataFrame

---

**Question 9** — *Multiple Choice*

Which type of join returns only the rows that have matching keys in both DataFrames?

- Inner join
- Left join
- Right join
- Outer join

---

**Question 10** — *Multiple Choice*

If you perform a left join between `df1` and `df2`, which rows will always be in the result?

- Only rows that match in both DataFrames
- All rows from `df1`
- All rows from `df2`
- All rows from both DataFrames

---

**Question 11** — *Multiple Choice*

When using `merge()` in Pandas without specifying `on=`, how does Pandas decide which columns to join on?

- It joins on columns with the same name in both DataFrames
- It joins on the first column in each DataFrame
- It requires you to specify the key column every time
- It throws an error
