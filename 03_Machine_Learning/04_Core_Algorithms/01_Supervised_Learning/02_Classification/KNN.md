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

