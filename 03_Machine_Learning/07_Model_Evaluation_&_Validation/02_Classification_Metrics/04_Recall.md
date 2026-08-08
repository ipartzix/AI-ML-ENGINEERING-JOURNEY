# Recall

## Definition

Recall is a classification evaluation metric that measures how many of the **actual Positive samples** were correctly identified by the model.

It answers:

> **"Of all the actual Positive cases, how many did the model correctly find?"**

Recall focuses on **False Negatives (FN)**.

Recall is also called:

- **Sensitivity**
- **True Positive Rate (TPR)**

---

# Formula

\[
Recall =
\frac{TP}{TP+FN}
\]

Where:

- \(TP\) = True Positive
- \(FN\) = False Negative

---

# Understanding Recall

From the confusion matrix:

| | Actual Positive | Actual Negative |
|---|---:|---:|
| **Predicted Positive** | **TP** | FP |
| **Predicted Negative** | **FN** | TN |

Recall considers the **Actual Positive** column:

\[
Recall =
\frac{\text{Correctly Identified Positives}}
{\text{All Actual Positives}}
\]

Therefore:

\[
Recall =
\frac{TP}{TP+FN}
\]

---

# Step-by-Step Example

Suppose a classification model produces:

```text
TP = 80
FN = 20
```

The dataset contains 100 actual Positive samples:

\[
TP+FN=80+20=100
\]

Now calculate Recall:

\[
Recall =
\frac{80}{80+20}
\]

\[
Recall =
\frac{80}{100}
\]

\[
Recall = 0.80
\]

Therefore:

\[
\boxed{Recall = 80\%}
\]

This means:

> The model successfully identified **80% of all actual Positive samples**.

The remaining **20% were False Negatives**.

---

# High Recall

A model has high Recall when it produces **few False Negatives**.

For example:

```text
TP = 95
FN = 5
```

\[
Recall =
\frac{95}{95+5}
=95\%
\]

The model detects most of the actual Positive cases.

---

# Low Recall

A model has low Recall when it misses many actual Positive cases.

For example:

```text
TP = 50
FN = 50
```

\[
Recall =
\frac{50}{50+50}
=50\%
\]

The model detects only half of the actual Positive cases.

---

# Recall and False Negatives

Recall is directly affected by False Negatives.

\[
Recall =
\frac{TP}{TP+FN}
\]

If **FN increases** while TP remains constant:

\[
Recall \downarrow
\]

If **FN decreases** while TP remains constant:

\[
Recall \uparrow
\]

Therefore:

> **High Recall means fewer actual Positive cases are missed.**

---

# Example: Disease Detection

Suppose 100 patients actually have a disease.

The model identifies:

```text
90 → Disease
10 → No Disease
```

Therefore:

```text
TP = 90
FN = 10
```

Recall:

\[
Recall =
\frac{90}{90+10}
\]

\[
Recall=90\%
\]

The model successfully detected **90% of the patients who actually had the disease**.

The remaining 10% were missed:

```text
FN = 10
```

In medical screening, missing a disease can be costly, so high Recall is often important.

---

# When Is Recall Important?

Recall is important when **False Negatives are costly**.

Examples:

### Disease Detection

```text
Actual Disease
        ↓
Model predicts No Disease
        ↓
False Negative
```

Missing a genuine disease case can be more costly than incorrectly flagging a healthy person.

---

### Fraud Detection

If the objective is to identify as many fraudulent transactions as possible, missing fraudulent transactions is costly.

High Recall helps reduce missed fraud cases.

---

### Security Threat Detection

If the model is detecting potentially dangerous or malicious events, failing to identify a real threat can be costly.

High Recall may therefore be prioritized.

---

# When to Prioritize Recall

Prioritize Recall when:

> **False Negatives are more costly than False Positives.**

For example:

```text
False Negative → Very costly
False Positive → Less costly
```

Then we generally want:

\[
Recall \uparrow
\]

---

# Recall vs Precision

Precision and Recall answer different questions.

### Precision

> Of everything the model predicted as Positive, how much was actually Positive?

\[
Precision =
\frac{TP}{TP+FP}
\]

Precision focuses on **False Positives**.

### Recall

> Of everything that was actually Positive, how much did the model find?

\[
Recall =
\frac{TP}{TP+FN}
\]

Recall focuses on **False Negatives**.

| Precision | Recall |
|---|---|
| Focuses on FP | Focuses on FN |
| Reliability of Positive predictions | Ability to find actual Positives |
| "How correct are my Positive predictions?" | "How many actual Positives did I find?" |

---

# Example: Precision vs Recall

Suppose:

```text
TP = 80
FP = 20
FN = 10
```

### Precision

\[
Precision =
\frac{80}{80+20}
\]

\[
Precision=80\%
\]

### Recall

\[
Recall =
\frac{80}{80+10}
\]

\[
Recall\approx88.89\%
\]

Therefore:

```text
Precision = 80%
Recall    = 88.89%
```

The model finds most actual Positive cases, but some of its Positive predictions are incorrect.

---

# Recall and Classification Threshold

For probability-based classification models, Recall depends on the **classification threshold**.

For example:

```text
Probability >= 0.5 → Positive
Probability < 0.5  → Negative
```

If the threshold is reduced:

```text
0.5 → 0.3
```

the model becomes more willing to predict Positive.

This can:

```text
Increase Positive Predictions
        ↓
Potentially reduce FN
        ↓
Recall may increase
```

However, it may also increase False Positives and reduce Precision.

Therefore:

> Precision and Recall usually involve a trade-off.

---

# Precision-Recall Trade-Off

Conceptually:

```text
Lower Threshold
       ↓
More Positive Predictions
       ↓
Usually fewer FN
       ↓
Recall may increase
       ↓
But FP may increase
       ↓
Precision may decrease
```

The exact behavior depends on the model and dataset.

---

# Recall and F1-Score

F1-Score combines Precision and Recall using the harmonic mean.

\[
F1 =
2\times
\frac{Precision\times Recall}
{Precision+Recall}
\]

A model cannot achieve a high F1-Score if either Precision or Recall is very low.

F1-Score is useful when both:

```text
False Positives
        +
False Negatives
```

are important.

---

# Recall and Specificity

Recall and Specificity focus on different actual classes.

### Recall

Measures how well the model identifies **actual Positive samples**.

\[
Recall =
\frac{TP}{TP+FN}
\]

Also:

\[
Recall = TPR
\]

### Specificity

Measures how well the model identifies **actual Negative samples**.

\[
Specificity =
\frac{TN}{TN+FP}
\]

Also:

\[
Specificity = TNR
\]

| Metric | Focus |
|---|---|
| Recall / Sensitivity / TPR | Actual Positive samples |
| Specificity / TNR | Actual Negative samples |

---

# False Negative Rate

False Negative Rate (FNR) measures the proportion of actual Positive samples that the model incorrectly predicts as Negative.

\[
FNR =
\frac{FN}{FN+TP}
\]

There is an important relationship:

\[
FNR = 1-Recall
\]

Therefore:

\[
Recall + FNR = 1
\]

Example:

If:

\[
Recall=0.90
\]

Then:

\[
FNR=1-0.90=0.10
\]

So:

```text
Recall = 90%
FNR    = 10%
```

---

# Recall in Multiclass Classification

For multiclass classification, Recall can be calculated separately for each class.

Example:

```text
Classes:
Cat
Dog
Horse
```

For the **Cat** class:

```text
TP = Cat correctly predicted as Cat
FN = Actual Cat incorrectly predicted as Dog or Horse
```

Then:

\[
Recall_{Cat}
=
\frac{TP_{Cat}}
{TP_{Cat}+FN_{Cat}}
\]

The same calculation can be performed for Dog and Horse.

---

# Macro, Micro and Weighted Recall

For multiclass classification, Recall can be averaged in different ways.

## Macro Recall

Calculate Recall for every class and take the unweighted average.

\[
Recall_{macro}
=
\frac{R_1+R_2+\cdots+R_k}{k}
\]

Every class receives equal importance.

Useful when:

> Every class is equally important.

---

## Weighted Recall

Calculate Recall for every class and take a weighted average based on the number of actual samples in each class.

Larger classes have greater influence.

Useful when:

> Class sizes are different and you want the class distribution reflected.

---

## Micro Recall

Combine the contributions of all classes before calculating Recall.

\[
Recall_{micro}
=
\frac{\sum TP}
{\sum TP+\sum FN}
\]

Useful when:

> You want an overall metric across all individual predictions.

---

# Python Example

```python
from sklearn.metrics import recall_score

y_true = [1, 1, 1, 0, 0, 0, 1, 0]
y_pred = [1, 1, 0, 1, 0, 0, 1, 0]

recall = recall_score(y_true, y_pred)

print("Recall:", recall)
```

Output:

```text
Recall: 0.75
```

Therefore:

\[
Recall=75\%
\]

---

# Recall from a Confusion Matrix

Suppose:

```text
TP = 30
FP = 10
FN = 5
TN = 55
```

The confusion matrix is:

| | Actual Positive | Actual Negative |
|---|---:|---:|
| **Predicted Positive** | 30 | 10 |
| **Predicted Negative** | 5 | 55 |

Recall:

\[
Recall =
\frac{30}{30+5}
\]

\[
Recall =
\frac{30}{35}
\]

\[
Recall\approx0.857
\]

\[
\boxed{Recall\approx85.7\%}
\]

---

# Advantages

- Directly measures the model's ability to find actual Positive cases.
- Especially useful when False Negatives are costly.
- Easy to interpret.
- Very useful for imbalanced classification problems when the Positive class is important.

---

# Disadvantages

- Does not directly consider False Positives.
- High Recall does not necessarily mean high Precision.
- A model can achieve high Recall by predicting many samples as Positive.
- Should usually be evaluated together with Precision and F1-Score.

---

# Recall vs Other Metrics

| Metric | Focus | Better |
|---|---|---|
| Accuracy | Overall correct predictions | Higher |
| Precision | Correct Positive predictions | Higher |
| Recall | Actual Positives detected | Higher |
| Specificity | Actual Negatives detected | Higher |
| F1-Score | Balance of Precision and Recall | Higher |
| FNR | Missed Positive cases | Lower |

---

# Key Points

- Recall measures the **ability to identify actual Positive samples**.
- Formula:

\[
Recall =
\frac{TP}{TP+FN}
\]

- Recall focuses on **False Negatives**.
- High Recall means **fewer actual Positive cases are missed**.
- Recall is also called:
  - Sensitivity
  - True Positive Rate (TPR)
- Recall is important when False Negatives are costly.
- Lowering the classification threshold can often increase Recall but may reduce Precision.
- For multiclass classification, use **macro, micro, or weighted Recall** depending on the problem.
- Recall should usually be considered together with **Precision and F1-Score**.