# Module 11 Overview: Tree-Based Models and Feature Importance

## Module Topic

Welcome to Module 11, where you'll discover one of the most powerful and widely-used families of machine learning algorithms: tree-based models. While linear and logistic regression assume the world works in straight lines, real business data is messy—filled with threshold effects, complex interactions, and non-linear relationships. Decision trees think differently: they learn by asking yes-or-no questions, just like a doctor diagnosing a patient or a loan officer evaluating an application. This week, you'll learn how single decision trees make predictions through intuitive if-then rules, then discover how random forests combine hundreds of these trees into prediction powerhouses that consistently outperform simpler approaches.

But accuracy alone isn't enough in business. When your model predicts that a customer will churn or a tumor is malignant, stakeholders need to know *why*. This is where feature importance becomes critical. You'll learn techniques to identify which variables drive your model's decisions—revealing that credit card balance matters far more than income for predicting defaults, or that cell size is the key indicator of breast cancer. These insights don't just build trust; they translate statistical patterns into actionable business strategy. By week's end, you'll command tools used daily by data scientists at banks assessing credit risk, hospitals predicting readmissions, and retailers modeling customer behavior.

Whether you're predicting house prices, diagnosing diseases, or identifying at-risk customers, tree-based models offer a sweet spot: sophisticated enough to capture complex patterns, yet interpretable enough to explain to executives, physicians, and regulators. Let's explore how trees make decisions—and how to understand the decisions they make.

---

### 🎯 Learning Objectives
By the end of this module, you will be able to:
- Explain how decision trees make predictions through recursive splitting using yes-or-no questions about features
- Understand the CART algorithm and how it uses Gini impurity (classification) or MSE (regression) to find optimal splits
- Build both classification and regression trees using scikit-learn's `DecisionTreeClassifier` and `DecisionTreeRegressor`
- Construct random forest models that combine bootstrap aggregating and feature randomness to improve prediction accuracy and stability
- Control tree complexity and prevent overfitting using hyperparameters like `max_depth`, `min_samples_split`, and `n_estimators`
- Calculate and interpret feature importance using both impurity-based and permutation-based methods
- Create and interpret partial dependence plots (PDPs) to understand how individual features influence predictions
- Apply tree-based methods and interpretability techniques to real-world classification and regression problems

---

### ✅ What You'll Learn This Week
- **How decision trees discover patterns**: Unlike linear models that assume straight-line relationships, trees automatically find threshold effects, non-linear patterns, and feature interactions by learning optimal yes-or-no questions from your data
- **Why random forests outperform single trees**: Bootstrap sampling creates diverse trees trained on different data samples, while feature randomness forces trees to explore different variable combinations—errors cancel out when predictions are averaged
- **The accuracy-interpretability tradeoff**: As models become more powerful (linear regression → decision trees → random forests), they become harder to explain—but feature importance techniques help you peek inside the black box
- **Which features drive predictions**: Permutation importance reveals which variables actually matter for your model's decisions by measuring performance drops when features are shuffled
- **How features influence outcomes**: Partial dependence plots (PDPs) show the relationship between important features and predictions, revealing whether effects are linear, have thresholds, or exhibit diminishing returns
- **Real-world applications**: Tree-based models excel at credit risk assessment, medical diagnosis, customer churn prediction, fraud detection, and any problem where stakeholders need both accuracy and explanation

---

### 🛠 How You'll Practice
- **Tuesday Lecture**: Tree-Based Models—Decision Trees, Random Forests, and Feature Importance
  - Visualize how linear models struggle with non-linear patterns, threshold effects, and complex feature interactions
  - Build your first decision tree for credit default prediction and trace through its if-then decision rules
  - Understand the CART algorithm's split-selection process using Gini impurity as a "messiness meter"
  - Explore the problems with single trees (instability and overfitting) through live code demonstrations
  - Discover how bootstrap aggregating and feature randomness transform unstable trees into robust random forests
  - Compare single decision trees vs. random forests on Boston housing data to see ensemble power in action
  - Extract and visualize feature importance to identify which variables drive housing price predictions
  - Create partial dependence plots to understand how the most important features influence model predictions

- **Thursday Lab**: Hands-On Practice with Decision Trees, Random Forests, and Feature Importance
  - **Part 1 (TA-led)**: Follow along as your TA demonstrates the complete tree-based modeling workflow using Boston housing data for regression
  - **Part 2 (Group work)**: Apply tree-based methods independently to breast cancer classification data
  - Build decision trees with varying depths to explore the bias-variance tradeoff and understand overfitting
  - Construct and tune random forest models by experimenting with hyperparameters (`n_estimators`, `max_depth`, `max_features`)
  - Compare model performance across different configurations to select the best approach for medical diagnosis
  - Calculate permutation importance to identify which cell characteristics most strongly predict malignancy
  - Create partial dependence plots to understand how key features like cell radius influence cancer probability
  - Document your model selection reasoning, balancing accuracy with computational efficiency and interpretability

---

### 📂 Lectures & Other Supplemental Files

TBD

---
