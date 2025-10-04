# Week 10

Hi everyone,

Hope you're having a great week and are ready to take your data science skills to the next level! In Week 10, we're making a crucial transition from predicting numbers to predicting categories—unlocking an entirely new world of business applications. You'll master techniques that drive critical decisions in finance, healthcare, marketing, and beyond.

Here's what you'll be learning:

• How to distinguish between regression and classification problems and why they require different approaches
• How to build logistic regression models that predict probabilities and categories for real business decisions
• How to evaluate classification models using sophisticated metrics that align with business costs and priorities
• How to avoid the "accuracy trap" and choose evaluation methods that provide genuine business value

These skills will transform how you approach business problems—moving from understanding what happened to predicting what will happen and making data-driven decisions about approval, diagnosis, targeting, and risk assessment.

🚀 **Get Started**: Jump into Module 10 to begin this week's lessons and activities.

‼️ **Important Note**: This week's lab will also serve as your homework assignment. During Thursday's lab, you'll work through hands-on challenges with real medical datasets, and your results will be used for assessment. Come prepared to dive deep into classification analysis!

🗣️ **Discussions & Feedback**: Don't forget, if you have any questions about course topics be sure to use the discussion board!

Cheers, Brad

---

# Module 10 Overview: Logistic Regression and Classification Evaluation

## Module Topic

This week transitions from predicting continuous values to predicting categories—a fundamental shift that opens up entirely new business applications. You'll master **logistic regression**, the foundational algorithm for classification problems, and learn sophisticated techniques for evaluating classification models that align with real business objectives and costs.

In business, many critical decisions involve classification rather than regression: Will a customer default on their loan? Is this email spam? Should we approve this medical claim? Will this marketing campaign succeed? While these yes/no questions might seem simpler than predicting exact dollar amounts, they present unique challenges that require specialized tools and evaluation frameworks. You'll discover why accuracy can be deeply misleading and learn to choose evaluation metrics that match your business priorities.

This module builds directly on your regression foundations while introducing powerful new concepts like precision-recall trade-offs, ROC curves, and business-aligned evaluation frameworks. These skills are essential for credit risk modeling, medical diagnosis support, fraud detection, and countless other applications where classification drives business value.

---

### 🎯 Learning Objectives
By the end of this module, you will be able to:
- Distinguish between regression and classification problems and explain why linear regression fails for categorical outcomes
- Understand the logistic function and how it transforms linear combinations into valid probabilities between 0 and 1
- Build and interpret logistic regression models using scikit-learn, including coefficient interpretation in terms of odds and business impact
- Apply logistic regression to real business scenarios using proper data preparation and train/test evaluation methodology
- Identify the "accuracy trap" in imbalanced datasets and explain why 97% accuracy can be misleading for business decisions
- Construct and interpret confusion matrices to understand exactly how classification models make errors
- Calculate and apply precision, recall, and F1-score metrics based on specific business contexts and error costs
- Use ROC curves and AUC to evaluate model ranking quality for risk-based pricing and customer stratification
- Design business-aligned evaluation frameworks that select appropriate metrics based on specific costs and connect model performance to real-world outcomes

---

### ✅ What You'll Learn This Week
- **Classification Fundamentals**: When to predict categories vs. continuous values, and why logistic regression solves problems that linear regression cannot handle
- **Logistic Function Mastery**: How the S-shaped sigmoid curve transforms any real number into valid probabilities, enabling business risk assessment
- **Probability, Odds, and Log-Odds**: Converting between these three related concepts and interpreting logistic regression coefficients in business terms
- **Model Building Workflow**: Complete end-to-end process from data preparation through dummy encoding to model training and prediction
- **Beyond Accuracy**: Why accuracy fails with imbalanced datasets and how to avoid the "high accuracy, zero business value" trap
- **Confusion Matrix Analysis**: Breaking down model performance into True/False Positives/Negatives and connecting these to business costs
- **Precision vs. Recall Trade-offs**: Understanding when to prioritize avoiding false alarms vs. catching all important cases
- **ROC-AUC for Risk Ranking**: Evaluating how well models rank customers from low-risk to high-risk for pricing and decision strategies
- **Business-Aligned Evaluation**: Systematic frameworks for choosing evaluation metrics based on error costs and business objectives

---

### 🛠 How You'll Practice
- **Tuesday Lecture**: Introduction to Logistic Regression and Classification Evaluation  
  Interactive exploration of classification vs. regression problems, hands-on logistic regression modeling with the Default dataset, coefficient interpretation in business context, and introduction to classification evaluation metrics beyond accuracy

- **Thursday Lab**: Hands-On Classification Analysis with Medical Data  
  Complete logistic regression workflow using the Breast Cancer Wisconsin dataset, data preparation with feature selection and dummy encoding, model training and evaluation using multiple metrics, comparison of different feature sets and their impact on performance, business cost analysis for medical diagnosis decisions, and independent analysis building models with progressively complex feature sets

---

### 📂 Lectures & Other Supplemental Files

**Required Readings:**
- **Chapter 23: Introduction to Logistic Regression for Classification** - Master the fundamentals of logistic regression, from understanding why linear regression fails for classification to building and interpreting your first logistic regression models
- **Chapter 24: Evaluating Classification Models** - Learn sophisticated evaluation techniques that go far beyond accuracy, including precision, recall, F1-score, ROC curves, and business-aligned evaluation frameworks

**Assessments:**
- **Reading Quiz**: Available Monday through Wednesday, covers key concepts from both chapters with business-focused scenarios
- **Week 10 Lab**: Serves as both Thursday's class session and this week's homework assignment, featuring hands-on classification analysis with real medical data

**Companion Notebooks:**
- [Chapter 23 Logistic Regression Notebook](https://colab.research.google.com/github/bradleyboehmke/uc-bana-4080/blob/main/example-notebooks/23_logistic_regression.ipynb) - Follow along with interactive code examples
- [Chapter 24 Classification Evaluation Notebook](https://colab.research.google.com/github/bradleyboehmke/uc-bana-4080/blob/main/example-notebooks/24_classification_evaluation.ipynb) - Hands-on practice with evaluation metrics

---