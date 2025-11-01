# Module 12 Overview: The Professional ML Workflow

## Module Topic

Up to this point, you've learned the fundamentals of building machine learning models—from linear regression to decision trees to random forests. You've split data into training and test sets, fit models, and evaluated their performance. But here's an uncomfortable truth: **we've been breaking a fundamental rule of production machine learning**. Every time you compared different model settings, tuned hyperparameters, or selected between models based on test set performance, you were "peeking" at the test set—and each peek made your performance estimates less trustworthy.

This week, you'll learn the **professional workflow** that data scientists use in production environments. You'll discover how **cross-validation** solves the test set contamination problem by giving you unlimited "practice tests" while keeping your final evaluation pristine. You'll master **hyperparameter tuning** techniques that systematically find optimal model configurations instead of relying on guesswork. And you'll explore **feature engineering**—the art of transforming raw data into powerful inputs that help models learn better patterns. These three topics are what separate beginner data scientists from professionals who build reliable, production-ready models.

By the end of this week, you'll understand not just *how* to build models, but how to build them the *right way*—with honest performance estimates, optimized configurations, and well-engineered features. These are the skills that will make you valuable to employers and ensure your models perform well on real business problems, not just classroom exercises.

---

### 🎯 Learning Objectives
By the end of this module, you will be able to:
- Explain why repeatedly evaluating models on the test set leads to test set contamination and optimistically biased performance estimates
- Implement k-fold cross-validation using scikit-learn to compare models without touching the test set
- Apply the five-stage proper ML workflow: split data, use CV for all decisions, select best approach, retrain on full training set, and evaluate on test set ONCE
- Explain the bias-variance tradeoff and identify symptoms of underfitting versus overfitting in model results
- Use GridSearchCV to systematically find optimal hyperparameter combinations across multiple parameters
- Apply encoding strategies for categorical variables (dummy/one-hot, label, and ordinal encoding) based on variable type and model choice
- Scale numerical features using StandardScaler or MinMaxScaler when appropriate for distance-based or regularized algorithms
- Build end-to-end feature engineering pipelines with scikit-learn to prevent data leakage and ensure reproducible workflows

---

### ✅ What You'll Learn This Week
- **Cross-validation**: How to evaluate and compare models using k-fold CV instead of repeatedly peeking at the test set, ensuring honest performance estimates
- **The proper workflow**: The five-stage process that keeps your test set pristine while using cross-validation to guide all modeling decisions
- **Bias-variance tradeoff**: Understanding how model complexity affects underfitting (high bias) versus overfitting (high variance), and finding the sweet spot
- **Grid search**: Systematically exploring all combinations of hyperparameters using GridSearchCV with built-in cross-validation
- **Encoding techniques**: Converting categorical variables to numerical format using dummy encoding, label encoding, or ordinal encoding based on your data and model
- **Feature scaling**: Standardizing features with StandardScaler or MinMaxScaler for algorithms sensitive to feature magnitude
- **Pipeline workflows**: Building reproducible, leak-free feature engineering pipelines that apply transformations correctly to training and test data
- **Real-world application**: How these professional techniques ensure your models perform reliably in production, not just in development

---

### 🛠 How You'll Practice
- **Tuesday Lecture**: The Professional ML Workflow
  - Compare the "wrong way" (repeated test set peeking) versus the "right way" (cross-validation workflow) with visual flowcharts
  - See k-fold cross-validation in action with hands-on Python code demonstrating 5-fold CV on the Ames housing dataset
  - Explore the bias-variance tradeoff through KNN visualization showing underfitting, balanced fit, and overfitting
  - Witness grid search systematically explore hyperparameter combinations and automatically find optimal settings
  - Watch live demonstrations of encoding categorical variables and scaling numerical features with before/after comparisons
  - Learn how pipelines prevent data leakage by ensuring transformations are fit on training data only
  - Participate in think-pair-share activities analyzing overfitting scenarios and real-world modeling decisions

- **Thursday Lab**: Hands-On Practice with CV, Tuning, and Feature Engineering
  - Implement k-fold cross-validation to compare multiple models (decision trees, random forests, logistic regression) on a business dataset
  - Use GridSearchCV to tune hyperparameters for a decision tree and random forest, exploring the parameter search space
  - Apply the complete five-stage workflow: split data, use CV for model selection and tuning, retrain on full training set, and evaluate on test set once
  - Engineer features for a real dataset: encode categorical variables, scale numerical features, and create new features based on domain knowledge
  - Build a scikit-learn pipeline that combines preprocessing and modeling steps to prevent data leakage
  - Analyze and interpret results: comparing cross-validation scores, understanding which hyperparameters matter most, and evaluating final test performance

---

### 📂 Lectures & Other Supplemental Files

TBD

---

## Canvas Announcement

Hi everyone,

Hope you're having a great week! We're entering Week 12—one of the most important weeks of the entire course. You've spent the past several weeks learning how to build machine learning models, and you've done great work. But this week, we're going to level up from "beginner data scientist" to "production-ready professional."

Here's what makes this week so valuable:

**Cross-validation**: You'll learn why repeatedly checking the test set makes your performance estimates unreliable, and how cross-validation solves this "peeking problem" to give you honest, trustworthy model evaluations.

**Hyperparameter tuning**: Instead of guessing which model settings to use, you'll master systematic techniques like GridSearchCV that automatically find optimal configurations by exploring the entire parameter space.

**Feature engineering**: You'll discover how to transform raw data into powerful features that help models learn better patterns—from encoding categories to scaling features to building leak-free pipelines.

**The professional workflow**: You'll put it all together into the five-stage workflow that data scientists use in production to ensure models perform reliably on real business problems, not just classroom exercises.

These are the skills that employers look for when hiring data scientists. Mastering this week's material will make you significantly more valuable in the job market and ensure your models perform well in the real world.

📌 Get Started: Jump into Module 12 on Canvas to begin this week's lessons and activities.

As we get closer to the end of the term, these advanced topics build on everything you've learned. Come to Tuesday's lecture ready to see the "right way" to build ML models, and come to Thursday's lab ready to apply these techniques hands-on.

As always, don't hesitate to reach out or post in the forums if you get stuck.

Cheers,
Brad
