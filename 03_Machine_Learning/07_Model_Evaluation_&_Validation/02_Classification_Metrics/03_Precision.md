# Precision

## Definition

Precision is a classification evaluation metric that measures how many of the samples predicted as **Positive** were actually Positive.

It answers:

> **"Of everything the model predicted as Positive, how much was actually Positive?"**

Precision focuses on **False Positives (FP)**.

---

# Formula

\[
Precision =
\frac{TP}{TP+FP}
\]

Where:

- \(TP\) = True Positive
- \(FP\) = False Positive

---

# Understanding Precision

From the confusion matrix:

| | Actual Positive | Actual Negative |
|---|---:|---:|
| **Predicted Positive** | **TP** | **FP** |
| **Predicted Negative** | FN | TN |

Precision considers only the **Predicted Positive** row:

\[
Precision =
\frac{\text{Correct Positive Predictions}}
{\text{All Positive Predictions}}
\]

Therefore:

\[
Precision =
\frac{TP}{TP+FP}
\]

---

# Step-by-Step Example

Suppose a classification model produces:

```text
TP = 80
FP = 20
```

The model predicted 100 samples as Positive:

\[
TP+FP=80+20=100
\]

Now calculate Precision:

\[
Precision =
\frac{80}{80+20}
\]

\[
Precision =
\frac{80}{100}
\]

\[
Precision = 0.80
\]

Therefore:

\[
\boxed{Precision = 80\%}
\]

This means:

> Out of all samples predicted as Positive, **80% were actually Positive**.

---

# Another Example

Suppose a spam detection model predicts 100 emails as spam.

Among them:

```text
80 → Actually spam
20 → Actually legitimate
```

Therefore:

```text
TP = 80
FP = 20
```

Precision:

\[
Precision =
\frac{80}{80+20}
=0.80
\]

\[
Precision=80\%
\]

So, when the model says:

```text
"Spam"
```

there is an **80% chance that the email is actually spam**, based on this evaluation result.

---

# High Precision

A model has high Precision when it produces **few False Positives**.

For example:

```text
TP = 95
FP = 5
```

\[
Precision =
\frac{95}{95+5}
=95\%
\]

The model's Positive predictions are highly reliable.

---

# Low Precision

A model has low Precision when it produces many False Positives.

For example:

```text
TP = 50
FP = 50
```

\[
Precision =
\frac{50}{50+50}
=50\%
\]

Half of the model's Positive predictions are incorrect.

---

# Precision and False Positives

Precision is directly affected by False Positives.

\[
Precision =
\frac{TP}{TP+FP}
\]

If **FP increases** while TP remains constant:

\[
Precision \downarrow
\]

If **FP decreases** while TP remains constant:

\[
Precision \uparrow
\]

Therefore:

> **High Precision means fewer False Positives among Positive predictions.**

---

# Precision vs Recall

Precision and Recall measure different things.

### Precision

> Of the samples I predicted as Positive, how many were actually Positive?

\[
Precision =
\frac{TP}{TP+FP}
\]

### Recall

> Of all the samples that were actually Positive, how many did I correctly identify?

\[
Recall =
\frac{TP}{TP+FN}
\]

| Precision | Recall |
|---|---|
| Focuses on FP | Focuses on FN |
| Reliability of Positive predictions | Ability to find actual Positives |
| "How correct are my Positive predictions?" | "How many Positives did I find?" |

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
=0.80
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

The model identifies most actual Positive cases, but some of its Positive predictions are incorrect.

---

# When Is Precision Important?

Precision is important when **False Positives are costly**.

Examples:

### Spam Detection

If the model predicts a legitimate email as spam:

```text
Actual       = Not Spam
Prediction   = Spam
             = FP
```

A high Precision model reduces the number of legitimate emails incorrectly marked as spam.

---

### Recommendation Systems

If a system recommends something as highly relevant when it is not relevant, that is a type of False Positive.

High Precision means the recommendations labeled Positive are more likely to actually be relevant.

---

### Fraud Detection

Depending on the system, incorrectly flagging legitimate transactions as fraudulent can create significant costs.

Higher Precision reduces unnecessary fraud alerts.

---

# When Precision Is More Important Than Recall

Prioritize Precision when:

> **False Positives are more costly than False Negatives.**

Example:

```text
False Positive → Very costly
False Negative → Less costly
```

Then we generally want:

\[
Precision \uparrow
\]

---

# Precision and Classification Threshold

For many classification models, Precision changes when the **classification threshold** changes.

For example:

```text
Probability >= 0.5 → Positive
Probability < 0.5  → Negative
```

If the threshold is increased:

```text
0.5 → 0.7
```

the model becomes more conservative about predicting Positive.

This can reduce False Positives and potentially increase Precision, but it may also increase False Negatives and reduce Recall.

Therefore:

> Precision and Recall usually involve a trade-off.

---

# Precision-Recall Trade-Off

A model can often increase Precision at the expense of Recall, or increase Recall at the expense of Precision.

Conceptually:

```text
Higher Threshold
       ↓
Fewer Positive Predictions
       ↓
Usually fewer FP
       ↓
Precision may increase
       ↓
But FN may increase
       ↓
Recall may decrease
```

The exact behavior depends on the model and dataset.

---

# Precision in Multiclass Classification

For multiclass classification, Precision can be calculated for each class.

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
FP = Non-Cat incorrectly predicted as Cat
```

Then:

\[
Precision_{Cat}
=
\frac{TP_{Cat}}
{TP_{Cat}+FP_{Cat}}
\]

The same calculation can be performed for Dog and Horse.

---

# Macro, Micro and Weighted Precision

For multiclass classification, Precision can be averaged in different ways.

## Macro Precision

Calculate Precision for every class and then take the unweighted average.

\[
Precision_{macro}
=
\frac{P_1+P_2+\cdots+P_k}{k}
\]

Every class receives equal importance.

Useful when:

> Every class is equally important.

---

## Weighted Precision

Calculate Precision for every class and take a weighted average based on the number of samples in each class.

Larger classes have greater influence.

Useful when:

> Class sizes are different and you want the class distribution reflected.

---

## Micro Precision

Combine the contributions of all classes before calculating Precision.

\[
Precision_{micro}
=
\frac{\sum TP}
{\sum TP+\sum FP}
\]

Useful when:

> You want an overall metric across all individual predictions.

---

# Python Example

```python
from sklearn.metrics import precision_score

y_true = [1, 1, 1, 0, 0, 0, 1, 0]
y_pred = [1, 1, 0, 1, 0, 0, 1, 0]

precision = precision_score(y_true, y_pred)

print("Precision:", precision)
```

Output:

```text
Precision: 0.75
```

Therefore:

\[
Precision=75\%
\]

---

# Precision from a Confusion Matrix

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

Precision:

\[
Precision =
\frac{30}{30+10}
\]

\[
Precision =
\frac{30}{40}
\]

\[
Precision=0.75
\]

\[
\boxed{Precision=75\%}
\]

---

# Advantages

- Directly measures the reliability of Positive predictions.
- Especially useful when False Positives are costly.
- Easy to interpret.
- Useful for imbalanced classification problems when Positive-class performance is important.

---

# Disadvantages

- Does not consider False Negatives directly.
- High Precision does not necessarily mean high Recall.
- Can be misleading if considered without understanding the classification threshold.
- Should usually be evaluated together with Recall and F1-Score.

---

# Precision vs Other Metrics

| Metric | Focus | Better |
|---|---|---|
| Accuracy | Overall correct predictions | Higher |
| Precision | Correct Positive predictions | Higher |
| Recall | Actual Positives detected | Higher |
| Specificity | Actual Negatives detected | Higher |
| F1-Score | Balance of Precision and Recall | Higher |
| FPR | Incorrect Positive predictions | Lower |

---

# Key Points

- Precision measures the **correctness of Positive predictions**.
- Formula:

\[
Precision =
\frac{TP}{TP+FP}
\]

- Precision focuses on **False Positives**.
- High Precision means **few False Positives among predicted Positives**.
- Precision is important when False Positives are costly.
- Precision and Recall are different metrics.
- Increasing the classification threshold can often increase Precision but may reduce Recall.
- For multiclass classification, use **macro, micro, or weighted Precision** depending on the problem.
- Precision should usually be considered together with **Recall and F1-Score**.