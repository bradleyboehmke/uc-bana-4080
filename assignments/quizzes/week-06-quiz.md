# Week 6 Reading Quiz

**Module:** 6 — Creating Efficient Code  
**Chapters:** 16 (Control Statements), 17 (Iteration Statements), 18 (Writing Functions)  
**Points:** 15 (1 pt per question)  
**Time limit:** 40 minutes  
**Attempts:** Up to 2 — final score is the average of both attempts

> Questions focus on conceptual knowledge and high-level comprehension rather
> than coding. If you don't feel confident after the first try, review the lesson
> materials and try again.

---

**Question 1** — *Multiple Choice*

You're building a customer loyalty program where VIP customers (those who spend $10,000+ annually) get 20% discount, Premium customers ($5,000–$9,999) get 15% discount, and Regular customers get 5% discount. Which code correctly implements this business logic?

- `if annual_spend >= 5000:` / `elif annual_spend >= 10000:` / `else: discount = 0.05`
- `if annual_spend >= 10000:` / `elif annual_spend >= 5000:` / `else: discount = 0.05`
- `if annual_spend > 10000:` / `elif annual_spend > 5000:` / `else: discount = 0.05`
- `if annual_spend >= 10000:` / `if annual_spend >= 5000:` / `else: discount = 0.15`

---

**Question 2** — *Multiple Choice*

Your e-commerce site needs to look up shipping costs based on 15 different shipping methods. Which approach would be MOST efficient and maintainable?

- Use a long if/elif/else chain with 15 conditions
- Use a dictionary with shipping methods as keys and costs as values
- Use nested if statements
- Use a while loop to check each option

---

**Question 3** — *Multiple Choice*

What will this code print?

```python
inventory_items = []
customer_complaints = 0
revenue_growth = 0.0

if inventory_items:
    print("A")
if customer_complaints:
    print("B")
if revenue_growth:
    print("C")
if not inventory_items:
    print("D")
```

- A B C D
- D only
- B C D
- Nothing will print

---

**Question 4** — *Multiple Choice*

You need to calculate tiered sales commission: 8% on sales over $50,000, and 5% on the first $50,000. Which code correctly calculates this?

- `commission = sales * 0.08` if `sales > 50000`, else `commission = sales * 0.05`
- `commission = 50000 * 0.05 + (sales - 50000) * 0.08` if `sales > 50000`, else `commission = sales * 0.05`
- `commission = min(sales, 50000) * 0.05 + max(0, sales - 50000) * 0.08`
- Both B and C are correct

---

**Question 5** — *Multiple Choice*

You're monitoring inventory levels that decrease daily due to sales. You want to stop when inventory drops below 100 units OR after 30 days, whichever comes first. Which loop type is most appropriate?

- For loop — because you know the maximum iterations (30 days)
- While loop — because the stopping condition depends on inventory level
- Either could work equally well
- List comprehension would be best

---

**Question 6** — *Multiple Choice*

You want to create a list of discounted prices where only products over $100 get a 20% discount; others keep their original price. Which list comprehension is correct?

- `[price * 0.8 for price in prices if price > 100]`
- `[price * 0.8 if price > 100 for price in prices]`
- `[price * 0.8 if price > 100 else price for price in prices]`
- `[price for price in prices if price * 0.8 > 100]`

---

**Question 7** — *Multiple Select*

You're writing a function to calculate customer lifetime value. Which parameter designs follow Python best practices? *(Select all that apply)*

- `def calculate_clv(revenue, margin, years, discount_rate=0.1)`
- `def calculate_clv(discount_rate=0.1, revenue, margin, years)`
- `def calculate_clv(revenue, margin, years=3, discount_rate=0.1)`
- `def calculate_clv(revenue, margin=0.2, years, discount_rate=0.1)`

---

**Question 8** — *Multiple Choice*

Which function is properly documented for business use?

- `def calc_roi(r, c): return (r - c) / c * 100`
- A function with a one-line docstring: `"""Calculates ROI percentage"""`
- A function with a full docstring including Args, Returns, and an Example
- All are equally good

---

**Question 9** — *Multiple Choice*

Your function calculates profit margins but sometimes receives invalid data. Which approach best handles this for business use?

- Let Python crash with its default error message
- Print error messages but continue running
- Use try/except to handle errors gracefully and provide business-friendly messages
- Ignore errors and return 0

---

**Question 10** — *Multiple Choice*

You want to categorize products by price range in a pandas DataFrame. Which approach is most appropriate?

- Write a full function for this simple categorization
- Use a lambda function with pandas `apply()`
- Use a for loop to process each row
- Use multiple if/elif statements

---

**Question 11** — *Multiple Choice*

What will this code print?

```python
profit_margin = 0.20

def calculate_profit(revenue):
    profit_margin = 0.15
    return revenue * profit_margin

result = calculate_profit(1000)
print(f"Global margin: {profit_margin}, Profit: {result}")
```

- Global margin: 0.15, Profit: 150
- Global margin: 0.20, Profit: 150
- Global margin: 0.15, Profit: 200
- This will cause an error

---

**Question 12** — *Match Each*

Match each task with the best approach:

**Tasks:**

1. Calculating profit margin for 100,000 transactions
2. Making API calls to different vendors
3. Processing daily sales files from multiple stores
4. Adding a "high value" flag to customer records

**Approaches:**

- A. For loop
- B. Pandas vectorized operation (`apply`, `np.where`)
- C. While loop
- D. List comprehension

---

**Question 13** — *Multiple Choice*

A customer is VIP (15% base discount), orders $600 (additional 5%), and is a loyalty member (additional 5%). The maximum total discount is 25%. What is their final discount?

- 15%
- 20%
- 25%
- 30%

---

**Question 14** — *Multiple Select*

Which statements about control flow best practices are true? *(Select all that apply)*

- Use `elif` instead of multiple `if` statements when conditions are mutually exclusive
- Dictionary lookups are generally faster than long if/elif chains
- Always include an `else` clause to handle unexpected cases
- Complex nested conditions should be avoided when possible
- Using meaningful variable names makes conditional logic easier to understand

---

**Question 15** — *Multiple Choice*

You're building a customer churn prediction system that processes customer data, applies business rules, and calculates risk scores for thousands of customers daily. Which combination of concepts would be most effective?

- Only use if/elif statements for all logic
- Use functions for reusable calculations, pandas vectorized operations for data processing, and dictionaries for business rule lookups
- Write everything in one long script with for loops
- Use only lambda functions for everything
