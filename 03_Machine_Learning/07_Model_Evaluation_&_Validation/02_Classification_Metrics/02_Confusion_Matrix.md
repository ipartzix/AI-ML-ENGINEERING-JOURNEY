# Confusion Matrix

## Definition

A Confusion Matrix is a table used to evaluate the performance of a **classification model** by comparing the model's predicted classes with the actual classes.

For binary classification, it contains four possible outcomes:

- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)

---

# Binary Classification Confusion Matrix

| | Actual Positive | Actual Negative |
|---|---:|---:|
| **Predicted Positive** | **TP** | **FP** |
| **Predicted Negative** | **FN** | **TN** |

The **rows represent predictions** and the **columns represent actual values**.

---

# 1. True Positive (TP)

A **True Positive** occurs when:

> The model predicts Positive and the actual class is Positive.

Example:

A model predicts:

```text
Disease = Yes
```

And the patient actually has the disease:

```text
Actual = Yes
```

Therefore:

```text
TP
```

---

# 2. True Negative (TN)

A **True Negative** occurs when:

> The model predicts Negative and the actual class is Negative.

Example:

```text
Predicted = No Disease
Actual    = No Disease
```

Therefore:

```text
TN
```

---

# 3. False Positive (FP)

A **False Positive** occurs when:

> The model predicts Positive, but the actual class is Negative.

Example:

```text
Predicted = Disease
Actual    = No Disease
```

Therefore:

```text
FP
```

This is also called a:

**Type I Error**

---

# 4. False Negative (FN)

A **False Negative** occurs when:

> The model predicts Negative, but the actual class is Positive.

Example:

```text
Predicted = No Disease
Actual    = Disease
```

Therefore:

```text
FN
```

This is also called a:

**Type II Error**

---

# Complete Example

Suppose a disease classification model produces the following results:

| | Actual Disease | Actual No Disease |
|---|---:|---:|
| **Predicted Disease** | 80 | 10 |
| **Predicted No Disease** | 5 | 105 |

Therefore:

```text
TP = 80
FP = 10
FN = 5
TN = 105
```

Total samples:

\[
80 + 10 + 5 + 105 = 200
\]

---

# Reading the Confusion Matrix

```text
                       Actual
                  Positive   Negative
                ┌──────────┬──────────┐
Predicted       │          │          │
Positive        │    TP    │    FP    │
                │    80    │    10    │
                ├──────────┼──────────┤
Negative        │    FN    │    TN    │
                │     5    │   105    │
                └──────────┴──────────┘
```

Correct predictions:

\[
TP + TN
\]

\[
80 + 105 = 185
\]

Incorrect predictions:

\[
FP + FN
\]

\[
10 + 5 = 15
\]

---

# Metrics Derived from the Confusion Matrix

The confusion matrix is the foundation for several classification metrics.

---

## Accuracy

Measures the proportion of all predictions that are correct.

\[
Accuracy =
\frac{TP + TN}
{TP + TN + FP + FN}
\]

For the example:

\[
Accuracy =
\frac{80+105}{200}
\]

\[
Accuracy = 0.925
\]

\[
Accuracy = 92.5\%
\]

---

## Precision

Measures how many predicted Positive samples were actually Positive.

\[
Precision =
\frac{TP}{TP+FP}
\]

For the example:

\[
Precision =
\frac{80}{80+10}
\]

\[
Precision \approx 88.89\%
\]

---

## Recall

Measures how many actual Positive samples were correctly identified.

\[
Recall =
\frac{TP}{TP+FN}
\]

For the example:

\[
Recall =
\frac{80}{80+5}
\]

\[
Recall \approx 94.12\%
\]

Recall is also called:

- Sensitivity
- True Positive Rate (TPR)

---

## Specificity

Measures how many actual Negative samples were correctly identified.

\[
Specificity =
\frac{TN}{TN+FP}
\]

For the example:

\[
Specificity =
\frac{105}{105+10}
\]

\[
Specificity \approx 91.30\%
\]

Specificity is also called:

**True Negative Rate (TNR)**

---

## F1-Score

F1-Score is the harmonic mean of Precision and Recall.

\[
F1 =
2\times
\frac{Precision\times Recall}
{Precision+Recall}
\]

It provides a balance between Precision and Recall.

---

# False Positive Rate

False Positive Rate measures the proportion of actual Negative samples incorrectly classified as Positive.

\[
FPR =
\frac{FP}{FP+TN}
\]

There is an important relationship:

\[
FPR = 1-Specificity
\]

---

# False Negative Rate

False Negative Rate measures the proportion of actual Positive samples incorrectly classified as Negative.

\[
FNR =
\frac{FN}{FN+TP}
\]

There is an important relationship:

\[
FNR = 1-Recall
\]

---

# Error Types

| Error | Meaning | Also Called |
|---|---|---|
| FP | Negative classified as Positive | Type I Error |
| FN | Positive classified as Negative | Type II Error |

---

# Why Confusion Matrix Is Important

Accuracy alone does not tell us **what type of mistakes** the model is making.

For example, two models may both have:

```text
Accuracy = 90%
```

But:

### Model A

```text
FP = 2
FN = 18
```

### Model B

```text
FP = 18
FN = 2
```

Both models have the same accuracy, but their behavior is very different.

Therefore, the confusion matrix allows us to understand:

- Which classes are being confused.
- How many false positives occur.
- How many false negatives occur.
- Whether the model is biased toward one class.
- Which classification metric should be prioritized.

---

# Confusion Matrix and Imbalanced Data

Confusion matrices are particularly important for **imbalanced datasets**.

Example:

```text
Total samples = 1000

Negative = 950
Positive = 50
```

A model that predicts every sample as Negative would achieve:

\[
Accuracy = \frac{950}{1000}=95\%
\]

But:

```text
TP = 0
FN = 50
```

The model identifies **none of the Positive cases**.

Therefore, the 95% accuracy is misleading.

The confusion matrix exposes this problem immediately.

---

# Binary vs Multiclass Confusion Matrix

## Binary Classification

There are two classes.

Example:

```text
Positive
Negative
```

The confusion matrix is:

\[
2\times2
\]

---

## Multiclass Classification

There are more than two classes.

Example:

```text
Cat
Dog
Horse
```

The confusion matrix becomes:

\[
3\times3
\]

Example:

| Actual / Predicted | Cat | Dog | Horse |
|---|---:|---:|---:|
| **Cat** | 45 | 3 | 2 |
| **Dog** | 4 | 42 | 4 |
| **Horse** | 1 | 5 | 44 |

### Diagonal

The diagonal represents **correct predictions**.

```text
45
42
44
```

### Off-Diagonal

The off-diagonal values represent **misclassifications**.

For example:

```text
Actual Cat → Predicted Dog = 3
```

---

# Python Example

```python
from sklearn.metrics import confusion_matrix

y_true = [
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 0
]

y_pred = [
    1, 1, 1, 0, 0,
    0, 0, 0, 1, 0
]

cm = confusion_matrix(y_true, y_pred)

print(cm)
```

Output:

```text
[[4 1]
 [2 3]]
```

Scikit-learn represents the binary confusion matrix as:

```text
[[TN, FP],
 [FN, TP]]
```

Therefore:

```text
TN = 4
FP = 1
FN = 2
TP = 3
```

---

# Visualizing the Confusion Matrix

```python
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

ConfusionMatrixDisplay.from_predictions(
    y_true,
    y_pred
)

plt.show()
```

---

# Normalized Confusion Matrix

A confusion matrix can also be normalized to show proportions or percentages instead of raw counts.

```python
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

ConfusionMatrixDisplay.from_predictions(
    y_true,
    y_pred,
    normalize="true"
)

plt.show()
```

`normalize="true"` normalizes each actual class.

---

# Key Relationships

The most important relationships to remember:

\[
Accuracy =
\frac{TP+TN}
{TP+TN+FP+FN}
\]

\[
Precision =
\frac{TP}{TP+FP}
\]

\[
Recall =
\frac{TP}{TP+FN}
\]

\[
Specificity =
\frac{TN}{TN+FP}
\]

\[
FPR =
\frac{FP}{FP+TN}
\]

\[
FNR =
\frac{FN}{FN+TP}
\]

---

# Quick Memory Trick

Think about the **prediction first**:

### Predicted Positive

- Actually Positive → **TP**
- Actually Negative → **FP**

### Predicted Negative

- Actually Positive → **FN**
- Actually Negative → **TN**

Or remember:

```text
TRUE  = Prediction is correct
FALSE = Prediction is wrong

POSITIVE = Model predicted Positive
NEGATIVE = Model predicted Negative
```

Therefore:

```text
TP → Correct Positive
TN → Correct Negative
FP → Wrong Positive
FN → Wrong Negative
```

---

# Key Takeaways

- Confusion Matrix is a fundamental tool for **classification evaluation**.
- It compares **actual classes** with **predicted classes**.
- Binary classification has four outcomes:
  - TP
  - TN
  - FP
  - FN
- Accuracy, Precision, Recall, Specificity, F1-Score, FPR, and FNR can be derived from it.
- The diagonal of a multiclass confusion matrix represents correct predictions.
- Off-diagonal values represent misclassifications.
- Confusion Matrix is especially important for **imbalanced datasets**.
- Never evaluate a classification model using Accuracy alone when class imbalance or unequal error costs matter.