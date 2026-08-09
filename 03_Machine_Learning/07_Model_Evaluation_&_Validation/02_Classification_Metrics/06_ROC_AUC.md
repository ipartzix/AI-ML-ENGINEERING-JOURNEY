# ROC-AUC

## Definition

ROC-AUC is a classification evaluation metric used to measure how well a model can **distinguish between different classes** across different classification thresholds.

It combines two concepts:

- **ROC Curve** → Receiver Operating Characteristic Curve
- **AUC** → Area Under the Curve

ROC-AUC is especially useful for evaluating binary classification models and comparing their ability to rank Positive samples higher than Negative samples.

---

# ROC Curve

The ROC Curve plots:

- **True Positive Rate (TPR)** on the Y-axis
- **False Positive Rate (FPR)** on the X-axis

Where:

\[
TPR = Recall =
\frac{TP}{TP+FN}
\]

and:

\[
FPR =
\frac{FP}{FP+TN}
\]

Therefore:

\[
Y = TPR
\]

\[
X = FPR
\]

---

# Why Do We Need a ROC Curve?

Most classification models produce a **probability** rather than directly producing a class.

For example:

```text
Sample A → 0.95
Sample B → 0.80
Sample C → 0.45
Sample D → 0.20
```

A threshold is then used to convert probabilities into classes.

For example:

```text
Threshold = 0.50

Probability >= 0.50 → Positive
Probability <  0.50 → Negative
```

But the threshold does not have to be 0.50.

It could be:

```text
0.10
0.20
0.30
...
0.90
```

Every threshold produces a different:

```text
TPR
FPR
```

The ROC Curve plots these values across different thresholds.

---

# Step-by-Step Example

Suppose a model produces the following probabilities:

| Sample | Actual | Predicted Probability |
|---|---:|---:|
| A | 1 | 0.90 |
| B | 1 | 0.80 |
| C | 0 | 0.70 |
| D | 1 | 0.60 |
| E | 0 | 0.40 |
| F | 0 | 0.30 |

The model ranks samples according to their predicted probability.

Now change the classification threshold.

---

## Threshold = 0.90

Predictions:

```text
A → Positive
B → Negative
C → Negative
D → Negative
E → Negative
F → Negative
```

This produces a particular:

```text
TPR
FPR
```

---

## Threshold = 0.70

Predictions:

```text
A → Positive
B → Positive
C → Positive
D → Negative
E → Negative
F → Negative
```

The TPR and FPR change.

---

## Threshold = 0.40

More samples are classified as Positive.

Again:

```text
TPR changes
FPR changes
```

Repeating this process for different thresholds generates the ROC Curve.

---

# True Positive Rate (TPR)

TPR measures how many actual Positive samples were correctly identified.

\[
TPR =
\frac{TP}{TP+FN}
\]

TPR is the same as:

\[
TPR = Recall = Sensitivity
\]

Higher TPR is better.

---

# False Positive Rate (FPR)

FPR measures how many actual Negative samples were incorrectly classified as Positive.

\[
FPR =
\frac{FP}{FP+TN}
\]

There is an important relationship:

\[
FPR = 1-Specificity
\]

Lower FPR is better.

---

# ROC Curve

A ROC Curve represents the relationship between:

\[
FPR
\]

and

\[
TPR
\]

Conceptually:

```text
TPR
1.0 |                 ●
    |              ●
    |           ●
    |        ●
    |     ●
    |  ●
0.0 +-------------------------
    0.0                     1.0
              FPR
```

A good classifier attempts to achieve:

```text
High TPR
+
Low FPR
```

Therefore, a good ROC Curve moves toward the **top-left corner**.

---

# What Is AUC?

AUC means:

> **Area Under the ROC Curve**

It summarizes the ROC Curve into a single number.

AUC measures how well the model can distinguish between Positive and Negative samples across different thresholds.

---

# AUC Interpretation

| ROC-AUC | General Interpretation |
|---:|---|
| 1.0 | Perfect discrimination |
| 0.9 – 1.0 | Excellent |
| 0.8 – 0.9 | Good |
| 0.7 – 0.8 | Acceptable |
| 0.6 – 0.7 | Weak |
| 0.5 | Random guessing |
| < 0.5 | Worse than random |

These ranges are general guidelines, not universal rules.

---

# Perfect Classifier

A perfect classifier has:

\[
TPR = 1
\]

and:

\[
FPR = 0
\]

Its ROC Curve reaches the top-left corner.

Therefore:

\[
ROC\text{-}AUC = 1.0
\]

---

# Random Classifier

A random classifier has approximately:

\[
TPR = FPR
\]

Its ROC Curve follows the diagonal line.

Therefore:

\[
ROC\text{-}AUC = 0.5
\]

A model with AUC = 0.5 has no useful class-discrimination ability.

---

# AUC < 0.5

If:

\[
AUC < 0.5
\]

the model performs worse than random ranking.

However, if the model's predictions are effectively reversed, flipping the prediction direction can produce:

\[
AUC' = 1-AUC
\]

For example:

\[
AUC=0.30
\]

would correspond to:

\[
1-0.30=0.70
\]

after reversing the ranking.

---

# Probability Interpretation of AUC

A useful interpretation of AUC is:

> The probability that the model assigns a higher prediction score to a randomly selected Positive sample than to a randomly selected Negative sample.

For example:

\[
AUC=0.85
\]

approximately means that the model ranks a randomly chosen Positive sample above a randomly chosen Negative sample **85% of the time**.

---

# ROC-AUC vs Accuracy

Accuracy evaluates predictions at **one particular classification threshold**.

ROC-AUC evaluates the model's discrimination ability across **many thresholds**.

| Accuracy | ROC-AUC |
|---|---|
| Uses a specific threshold | Considers many thresholds |
| Measures correct predictions | Measures class discrimination |
| Can be misleading with imbalance | Often more informative for ranking/discrimination |
| Depends strongly on threshold | Less dependent on a single threshold |

---

# ROC-AUC vs Precision

Precision:

\[
Precision =
\frac{TP}{TP+FP}
\]

ROC-AUC:

- Uses TPR and FPR.
- Evaluates different classification thresholds.
- Measures ranking/discrimination ability.

Precision is particularly useful when the proportion of Positive predictions matters.

ROC-AUC is useful when evaluating how well the model separates the classes across thresholds.

---

# ROC-AUC vs Recall

Recall:

\[
Recall =
\frac{TP}{TP+FN}
\]

Recall evaluates performance at a particular threshold.

ROC-AUC evaluates the model's discrimination behavior across thresholds.

---

# ROC-AUC and Imbalanced Data

ROC-AUC can be useful for imbalanced classification, but it should **not automatically be considered sufficient**.

When the Positive class is rare, a model may have a good ROC-AUC while still producing many False Positives at the operating threshold that matters in practice.

For highly imbalanced datasets, also consider:

- Precision
- Recall
- F1-Score
- Precision-Recall Curve
- PR-AUC

The appropriate metric depends on the problem and the cost of errors.

---

# ROC-AUC for Multiclass Classification

ROC-AUC can also be used for multiclass classification.

For example:

```text
Cat
Dog
Horse
```

A common approach is **One-vs-Rest (OvR)**.

For each class:

```text
Cat vs Not Cat
Dog vs Not Dog
Horse vs Not Horse
```

AUC can then be calculated for each class and averaged.

Common averaging methods include:

- Macro
- Weighted
- Micro

---

# Python Example

```python
from sklearn.metrics import roc_auc_score

y_true = [0, 0, 1, 1, 1, 0]

y_probability = [
    0.10,
    0.30,
    0.60,
    0.70,
    0.90,
    0.20
]

auc = roc_auc_score(y_true, y_probability)

print("ROC-AUC:", auc)
```

Output:

```text
ROC-AUC: 1.0
```

The model perfectly separates the Positive and Negative samples in this example.

---

# Plotting the ROC Curve

```python
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

fpr, tpr, thresholds = roc_curve(
    y_true,
    y_probability
)

plt.plot(fpr, tpr)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.show()
```

---

# ROC-AUC Directly from Scikit-Learn

```python
from sklearn.metrics import roc_auc_score

auc = roc_auc_score(
    y_true,
    y_probability
)

print("ROC-AUC:", auc)
```

Important:

```python
y_probability
```

should contain the model's **probability/score for the Positive class**, not the final predicted class labels.

Correct:

```python
y_probability = model.predict_proba(X_test)[:, 1]
```

Then:

```python
roc_auc_score(y_test, y_probability)
```

Incorrect for standard ROC-AUC calculation:

```python
y_pred = model.predict(X_test)

roc_auc_score(y_test, y_pred)
```

Using hard class predictions loses the threshold information that ROC-AUC is designed to evaluate.

---

# Logistic Regression Example

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

model = LogisticRegression()

model.fit(X_train, y_train)

y_probability = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(
    y_test,
    y_probability
)

print("ROC-AUC:", auc)
```

---

# Advantages

- Evaluates discrimination across multiple thresholds.
- Provides a single summary score.
- Useful for comparing classification models.
- Does not require choosing one classification threshold for the AUC calculation.
- Useful when the model outputs probability scores.

---

# Disadvantages

- Does not directly tell you the best classification threshold.
- Does not directly measure probability calibration.
- Can hide poor performance in the region of FPR/TPR that matters most.
- Can be less informative than Precision-Recall analysis for highly imbalanced datasets.
- A high ROC-AUC does not guarantee good real-world performance at a particular threshold.

---

# Key Points

- **ROC** = Receiver Operating Characteristic.
- **AUC** = Area Under the Curve.
- ROC Curve plots:

\[
TPR \text{ vs } FPR
\]

- TPR is the same as Recall:

\[
TPR =
\frac{TP}{TP+FN}
\]

- FPR is:

\[
FPR =
\frac{FP}{FP+TN}
\]

- AUC measures the model's ability to **discriminate between classes**.
- ROC-AUC = **1.0** → Perfect discrimination.
- ROC-AUC = **0.5** → Random performance.
- Higher ROC-AUC is generally better.
- ROC-AUC requires **prediction scores/probabilities**, not just hard class labels.
- For highly imbalanced problems, also inspect **Precision, Recall, F1-Score, and PR-AUC**.
- ROC-AUC evaluates discrimination; it does **not** tell you whether predicted probabilities are well calibrated.