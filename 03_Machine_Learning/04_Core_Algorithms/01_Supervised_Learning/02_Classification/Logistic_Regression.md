# Logistic Regression

## Introduction

Logistic Regression is a supervised machine learning algorithm used for **classification problems**. It predicts the probability that an input belongs to a particular class.

Examples:

* Email Spam Detection (Spam/Not Spam)
* Disease Prediction (Yes/No)
* Customer Churn Prediction

---

## Why Not Linear Regression?

Linear Regression predicts continuous values and can produce outputs less than 0 or greater than 1, which are not suitable for probabilities.

Logistic Regression uses the **Sigmoid Function** to convert outputs into probabilities between 0 and 1.

---

## Sigmoid Function

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

Where:

[
z = w_1x_1 + w_2x_2 + ... + w_nx_n + b
]

### Properties

* Output range: 0 to 1
* Produces probability values
* S-shaped curve

---

## Working of Logistic Regression

### Step 1: Calculate Linear Combination

[
z = wx + b
]

### Step 2: Apply Sigmoid Function

[
P(Y=1) = \frac{1}{1 + e^{-z}}
]

### Step 3: Make Prediction

* If probability ≥ 0.5 → Class 1
* If probability < 0.5 → Class 0

---

## Types of Logistic Regression

### 1. Binary Logistic Regression

Used when there are only two classes.

Examples:

* Pass/Fail
* Yes/No

### 2. Multinomial Logistic Regression

Used for more than two classes.

Examples:

* Red, Green, Blue

### 3. Ordinal Logistic Regression

Used when classes have an order.

Examples:

* Low, Medium, High

---

## Cost Function

Logistic Regression uses **Log Loss (Cross-Entropy Loss)**:

[
J(\theta) = -\frac{1}{m}
\sum
\left[
y\log(h_\theta(x))
+
(1-y)\log(1-h_\theta(x))
\right]
]

This function measures prediction error.

---

## Advantages

* Simple and easy to implement
* Fast training process
* Works well for binary classification
* Provides probability estimates
* Interpretable results

---

## Disadvantages

* Assumes a linear relationship between features and log-odds
* Sensitive to outliers
* Not suitable for highly complex datasets
* Performance decreases with many irrelevant features

---

## Applications

* Spam Email Detection
* Medical Diagnosis
* Credit Risk Analysis
* Customer Churn Prediction
* Fraud Detection
* Sentiment Analysis

---

## Summary

```Logistic Regression is a classification algorithm that uses the Sigmoid Function to predict probabilities between 0 and 1. It is widely used for binary classification tasks because it is simple, efficient, and easy to interpret.```
