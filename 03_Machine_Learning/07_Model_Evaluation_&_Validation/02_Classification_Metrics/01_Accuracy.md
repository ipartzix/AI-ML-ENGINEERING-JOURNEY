# Accuracy

## Definition

Accuracy is a classification evaluation metric that measures the proportion of predictions that a model classified correctly out of all predictions.

It answers:

> **"How many predictions did the model get correct?"**

---

## Formula

\[
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
\]

Where:

- \(TP\) = True Positive
- \(TN\) = True Negative
- \(FP\) = False Positive
- \(FN\) = False Negative

---

## Understanding the Confusion Matrix

| | Actual Positive | Actual Negative |
|---|---:|---:|
| **Predicted Positive** | TP | FP |
| **Predicted Negative** | FN | TN |

### True Positive (TP)

Model predicts **Positive**, and the actual class is **Positive**.

### True Negative (TN)

Model predicts **Negative**, and the actual class is **Negative**.

### False Positive (FP)

Model predicts **Positive**, but the actual class is **Negative**.

Also called a **Type I Error**.

### False Negative (FN)

Model predicts **Negative**, but the actual class is **Positive**.

Also called a **Type II Error**.

---

## Step-by-Step Example

Suppose a binary classification model makes **100 predictions**:

- TP = 40
- TN = 45
- FP = 5
- FN = 10

### Step 1: Calculate Correct Predictions

\[
TP + TN = 40 + 45 = 85
\]

### Step 2: Calculate Total Predictions

\[
TP + TN + FP + FN
\]

\[
= 40 + 45 + 5 + 10 = 100
\]

### Step 3: Calculate Accuracy

\[
Accuracy = \frac{85}{100}
\]

\[
Accuracy = 0.85
\]

Therefore:

\[
\boxed{Accuracy = 85\%}
\]

The model correctly classified **85 out of 100 samples**.

---

## Percentage Form

Accuracy can be represented as:

\[
Accuracy(\%) =
\frac{TP + TN}{TP + TN + FP + FN}
\times 100
\]

For the example:

\[
Accuracy = 0.85 \times 100 = 85\%
\]

---

## Interpretation

| Accuracy | Interpretation |
|---:|---|
| 1.00 (100%) | Perfect classification |
| 0.90 (90%) | 90% predictions are correct |
| 0.80 (80%) | 80% predictions are correct |
| 0.50 (50%) | Half of predictions are correct |

**Higher accuracy generally indicates better classification performance.**

However, accuracy alone can be misleading when the dataset is **imbalanced**.

---

## Accuracy and Imbalanced Data

Consider a dataset containing:

- 950 Negative samples
- 50 Positive samples

A model predicts **Negative for every sample**.

Then:

- TN = 950
- TP = 0
- FP = 0
- FN = 50

Accuracy:

\[
Accuracy =
\frac{950 + 0}{1000}
= 0.95
\]

\[
Accuracy = 95\%
\]

Although the accuracy is **95%**, the model completely fails to identify the Positive class.

Therefore, for imbalanced classification problems, accuracy should be considered together with metrics such as:

- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

---

## Advantages

- Simple to understand.
- Easy to calculate.
- Useful when classes are reasonably balanced.
- Provides a quick overall measure of classification correctness.

---

## Disadvantages

- Can be misleading for imbalanced datasets.
- Does not distinguish between FP and FN.
- Does not indicate which class the model performs poorly on.
- High accuracy does not necessarily mean a useful model.

---

## When to Use Accuracy

Accuracy is appropriate when:

- Classes are relatively balanced.
- False positives and false negatives have similar importance.
- You want a simple overall measure of correctness.

Avoid relying on accuracy alone when:

- The dataset is highly imbalanced.
- One class is much more important than another.
- False positives or false negatives have different costs.

---

## Python Example

```python
from sklearn.metrics import accuracy_score

y_true = [1, 1, 0, 0, 1, 0, 1, 0]
y_pred = [1, 0, 0, 0, 1, 1, 1, 0]

accuracy = accuracy_score(y_true, y_pred)

print("Accuracy:", accuracy)