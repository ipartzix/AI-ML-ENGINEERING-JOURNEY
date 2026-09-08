# K-Nearest Neighbors (KNN)

## Introduction

K-Nearest Neighbors (KNN) is a **supervised machine learning algorithm** used for **classification and regression problems**. It makes predictions based on the closest data points (neighbors) to a given input.

Examples:

* Customer Classification
* Disease Prediction
* Handwritten Digit Recognition
* Recommendation Systems

---

## Why KNN?

KNN is useful when similar data points are expected to have similar outputs.

For example, if most of the nearest customers to a new customer belong to the **"High Risk"** class, KNN will likely classify the new customer as **High Risk**.

KNN is called a **lazy learning algorithm** because it does not build an explicit model during training. It stores the training data and performs calculations when making predictions.

---

## How KNN Works

### Step 1: Choose the Value of K

Select the number of neighbors to consider.

Example:

```text
K = 3
```

This means the algorithm considers the **3 nearest data points**.

### Step 2: Calculate Distance

KNN calculates the distance between the new data point and existing training points.

The most commonly used distance is **Euclidean Distance**:

$$
d = \sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
$$

For two-dimensional data:

$$
d = \sqrt{(x_1-y_1)^2+(x_2-y_2)^2}
$$

### Step 3: Find K Nearest Neighbors

Select the **K data points with the smallest distances**.

### Step 4: Make Prediction

For classification, KNN uses **majority voting**.

Example:

```text
K = 5

Neighbor Classes:
A
A
B
A
B

Prediction = A
```

Because Class A occurs most frequently.

---

## Types of KNN

### 1. KNN Classification

Used when the target is a categorical class.

Examples:

* Spam / Not Spam
* Pass / Fail
* Cat / Dog

### 2. KNN Regression

Used when the target is a continuous numerical value.

Examples:

* House Price Prediction
* Temperature Prediction
* Salary Prediction

---

## Choosing the Value of K

The value of **K** significantly affects the performance of KNN.

### Small K

Example:

```text
K = 1
```

* Sensitive to noise
* Can lead to overfitting
* Complex decision boundary

### Large K

* Less sensitive to noise
* Can lead to underfitting
* Smoother decision boundary

A common approach is to test different K values and select the one that performs best using validation data.

---

## Feature Scaling

Feature scaling is **very important in KNN** because KNN is distance-based.

Suppose:

```text
Age:        20 – 60
Salary:     20,000 – 1,00,000
```

Salary can dominate the distance calculation because it has much larger numerical values.

Therefore, techniques such as:

* Standardization
* Min-Max Scaling

are commonly used before applying KNN.

---

## Distance Metrics

KNN can use different distance metrics to determine how close two data points are.

### 1. Euclidean Distance

Most commonly used for numerical data.

$$
d = \sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
$$

### 2. Manhattan Distance

Measures distance by summing absolute differences.

$$
d = \sum_{i=1}^{n}|x_i-y_i|
$$

### 3. Minkowski Distance

A generalized form of Euclidean and Manhattan distance.

$$
d = \left(\sum_{i=1}^{n}|x_i-y_i|^p\right)^{1/p}
$$

---

## Advantages

* Simple and easy to understand
* Easy to implement
* No complex training process
* Can be used for classification and regression
* Works well with smaller datasets
* Can model non-linear decision boundaries

---

## Disadvantages

* Prediction can be computationally expensive
* Requires feature scaling
* Sensitive to irrelevant features
* Sensitive to noisy data
* Performance decreases with very large datasets
* Choosing the correct K can be difficult

---

## Applications

* Recommendation Systems
* Pattern Recognition
* Medical Diagnosis
* Image Classification
* Customer Classification
* Fraud Detection
* Handwritten Digit Recognition

---

## Summary

K-Nearest Neighbors (KNN) is a **supervised, distance-based machine learning algorithm** used for classification and regression. It predicts the output of a new data point by examining its **K nearest neighbors**. KNN is simple and effective, but **feature scaling, K selection, and computational cost** are important considerations.
