# Bias–Variance Trade-off | Overfitting and Underfitting in Machine Learning

## 1. Core Idea

The **bias–variance trade-off** explains how model performance is affected by two types of errors:

* **Bias** → Error due to overly simple assumptions
* **Variance** → Error due to sensitivity to training data

### Total Error Formula

[
\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}
]

* **Irreducible Error**: Noise inherent in the data (cannot be reduced)

---

## 2. Bias (Underfitting)

### Definition

Bias occurs when the model is too simple to capture the underlying data patterns.

### Characteristics

* High training error
* High testing error
* Oversimplified assumptions

### Example

* Using linear regression for non-linear data

### Result

→ **Underfitting**

---

## 3. Variance (Overfitting)

### Definition

Variance occurs when the model learns noise along with actual patterns.

### Characteristics

* Very low training error
* High testing error
* Highly sensitive to training data

### Example

* High-degree polynomial regression fitting all data points

### Result

→ **Overfitting**

---

## 4. Visual Intuition

```
Model Complexity →

Underfitting -------- Optimal -------- Overfitting
   High Bias          Balanced         High Variance
   Low Variance                         Low Bias
```

---

## 5. Overfitting vs Underfitting

| Aspect           | Underfitting | Overfitting |
| ---------------- | ------------ | ----------- |
| Model Complexity | Too simple   | Too complex |
| Training Error   | High         | Very low    |
| Testing Error    | High         | High        |
| Bias             | High         | Low         |
| Variance         | Low          | High        |

---

## 6. Bias–Variance Trade-off Curve

* As **model complexity increases**:

  * Bias ↓
  * Variance ↑

* Goal: Find the **optimal balance point** where total error is minimized

---

## 7. How to Handle Underfitting

* Increase model complexity
* Add more features
* Reduce regularization
* Use more flexible models (e.g., decision trees, neural networks)

---

## 8. How to Handle Overfitting

* Apply **regularization (L1, L2)**
* Reduce model complexity
* Use **cross-validation**
* Increase training data
* Use techniques like:

  * Dropout (neural networks)
  * Pruning (decision trees)
  * Early stopping

---

## 9. Practical Insight

* High training accuracy does not guarantee good performance
* Focus on **generalization**
* Slight bias is often preferable to high variance

---

## 10. One-Line Summary

> A good model balances bias and variance to generalize well on unseen data.

---
