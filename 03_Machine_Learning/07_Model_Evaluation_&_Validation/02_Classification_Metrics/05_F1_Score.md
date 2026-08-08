# F1-Score

## Definition

F1-Score is a classification evaluation metric that combines **Precision** and **Recall** into a single score.

It is the **harmonic mean** of Precision and Recall.

F1-Score is useful when both **False Positives (FP)** and **False Negatives (FN)** are important.

It answers:

> **"How well does the model balance Precision and Recall?"**

---

# Formula

\[
F1 =
2\times
\frac{Precision\times Recall}
{Precision+Recall}
\]

Where:

- Precision = \(\frac{TP}{TP+FP}\)
- Recall = \(\frac{TP}{TP+FN}\)

The formula can also be written directly using the confusion matrix:

\[
F1 =
\frac{2TP}
{2TP+FP+FN}
\]

---

# Why Harmonic Mean?

F1-Score uses the **harmonic mean** rather than the arithmetic mean.

For two values \(P\) and \(R\):

\[
H =
\frac{2PR}{P+R}
\]

The harmonic mean gives more importance to the smaller value.

Therefore, a model needs both:

```text
High Precision
      +
High Recall
      ↓
High F1-Score
```

If either Precision or Recall is very low, the F1-Score will also be low.

---

# Step-by-Step Example

Suppose:

```text
TP = 80
FP = 20
FN = 10
```

## Step 1: Calculate Precision

\[
Precision =
\frac{TP}{TP+FP}
\]

\[
Precision =
\frac{80}{80+20}
\]

\[
Precision=0.80
\]

Therefore:

\[
Precision=80\%
\]

---

## Step 2: Calculate Recall

\[
Recall =
\frac{TP}{TP+FN}
\]

\[
Recall =
\frac{80}{80+10}
\]

\[
Recall =
\frac{80}{90}
\]

\[
Recall\approx0.889
\]

Therefore:

\[
Recall\approx88.9\%
\]

---

## Step 3: Calculate F1-Score

\[
F1 =
2\times
\frac{0.80\times0.889}
{0.80+0.889}
\]

\[
F1\approx0.842
\]

Therefore:

\[
\boxed{F1\approx84.2\%}
\]

---

# Direct Calculation from Confusion Matrix

Using:

```text
TP = 80
FP = 20
FN = 10
```

We can directly calculate:

\[
F1 =
\frac{2TP}
{2TP+FP+FN}
\]

\[
F1 =
\frac{2(80)}
{2(80)+20+10}
\]

\[
F1 =
\frac{160}{190}
\]

\[
F1\approx0.842
\]

\[
\boxed{F1\approx84.2\%}
\]

---

# Interpretation

| F1-Score | General Interpretation |
|---:|---|
| 1.0 | Perfect Precision and Recall |
| Close to 1.0 | Excellent balance |
| Around 0.8 | Good balance |
| Around 0.5 | Moderate |
| Close to 0 | Very poor |

F1-Score ranges from:

\[
0 \leq F1 \leq 1
\]

Higher F1-Score generally indicates better performance.

---

# F1-Score and Precision/Recall

Consider two models.

### Model A

```text
Precision = 0.95
Recall    = 0.40
```

### Model B

```text
Precision = 0.75
Recall    = 0.75
```

Although Model A has higher Precision, it has poor Recall.

Model B has a better balance between the two.

This is why F1-Score is useful when **both Precision and Recall matter**.

---

# F1-Score and Imbalanced Data

F1-Score is particularly useful for **imbalanced classification problems**.

Suppose:

```text
Negative = 950
Positive = 50
```

A model could achieve:

```text
Accuracy = 95%
```

by predicting every sample as Negative.

But the model would have:

```text
TP = 0
FN = 50
```

Therefore:

```text
Recall = 0
F1-Score = 0
```

This exposes the fact that the model completely fails to identify the Positive class.

Therefore:

> F1-Score can provide more useful information than Accuracy when the dataset is imbalanced.

---

# Precision vs Recall vs F1-Score

| Metric | Main Question | Focus |
|---|---|---|
| Precision | How many predicted Positives were actually Positive? | FP |
| Recall | How many actual Positives were found? | FN |
| F1-Score | How well are Precision and Recall balanced? | FP + FN |

### Precision

\[
Precision =
\frac{TP}{TP+FP}
\]

### Recall

\[
Recall =
\frac{TP}{TP+FN}
\]

### F1

\[
F1 =
2\times
\frac{Precision\times Recall}
{Precision+Recall}
\]

---

# When to Use F1-Score

Use F1-Score when:

- The dataset is imbalanced.
- Both False Positives and False Negatives matter.
- You need a balance between Precision and Recall.
- Accuracy alone does not adequately represent model performance.

---

# When F1-Score May Not Be Appropriate

F1-Score should not automatically be the primary metric for every problem.

For example:

### False Negatives Are Much More Costly

If missing a Positive case is significantly worse than producing a False Positive, prioritize:

\[
Recall
\]

rather than F1 alone.

### False Positives Are Much More Costly

If False Positives are significantly worse, prioritize:

\[
Precision
\]

rather than F1 alone.

The metric should reflect the **real-world cost of errors**.

---

# F1-Score and Classification Threshold

F1-Score depends on the classification threshold.

For example:

```text
Probability >= 0.5 → Positive
Probability < 0.5  → Negative
```

Changing the threshold changes:

```text
TP
FP
FN
TN
```

Therefore it also changes:

```text
Precision
Recall
F1-Score
```

A threshold can be selected to achieve a desirable balance between Precision and Recall.

---

# Multiclass F1-Score

For multiclass classification, F1-Score can be calculated separately for each class.

Example:

```text
Cat
Dog
Horse
```

For each class, that class is treated as the **Positive** class and all other classes are treated as **Negative**.

For example, for Cat:

```text
Positive = Cat
Negative = Dog + Horse
```

Then:

\[
F1_{Cat}
\]

can be calculated.

The same process is performed for Dog and Horse.

---

# Macro F1

Calculate F1-Score for every class and then take the unweighted average.

\[
F1_{macro}
=
\frac{F1_1+F1_2+\cdots+F1_k}{k}
\]

Every class receives equal importance.

Useful when:

> Every class is equally important.

---

# Weighted F1

Calculate F1-Score for every class and take a weighted average based on the number of actual samples in each class.

\[
F1_{weighted}
=
\frac{\sum_{i=1}^{k} n_iF1_i}
{\sum_{i=1}^{k}n_i}
\]

Where:

- \(F1_i\) = F1-Score of class \(i\)
- \(n_i\) = Number of actual samples in class \(i\)

Useful when:

> You want class frequency to influence the overall score.

---

# Micro F1

Combine the contributions of all classes before calculating the metric.

\[
F1_{micro}
=
\frac{2TP_{total}}
{2TP_{total}+FP_{total}+FN_{total}}
\]

Useful when:

> You want an overall measure based on individual predictions.

---

# Python Example

```python
from sklearn.metrics import f1_score

y_true = [1, 1, 1, 0, 0, 0, 1, 0]
y_pred = [1, 1, 0, 1, 0, 0, 1, 0]

f1 = f1_score(y_true, y_pred)

print("F1-Score:", f1)
```

Output:

```text
F1-Score: 0.7272727272727272
```

Therefore:

\[
F1\approx72.73\%
\]

---

# Multiclass Python Example

```python
from sklearn.metrics import f1_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 1, 0, 2, 2]

# Macro F1
f1_macro = f1_score(
    y_true,
    y_pred,
    average="macro"
)

# Weighted F1
f1_weighted = f1_score(
    y_true,
    y_pred,
    average="weighted"
)

# Micro F1
f1_micro = f1_score(
    y_true,
    y_pred,
    average="micro"
)

print("Macro F1    :", f1_macro)
print("Weighted F1 :", f1_weighted)
print("Micro F1    :", f1_micro)
```

---

# F1-Score vs Other Classification Metrics

| Metric | Measures | Better |
|---|---|---|
| Accuracy | Overall correctness | Higher |
| Precision | Reliability of Positive predictions | Higher |
| Recall | Ability to find actual Positives | Higher |
| F1-Score | Balance between Precision and Recall | Higher |
| Specificity | Ability to find actual Negatives | Higher |
| FPR | Incorrect Positive predictions | Lower |
| Log Loss | Quality of predicted probabilities | Lower |

---

# Advantages

- Balances Precision and Recall.
- Useful for imbalanced datasets.
- Provides a single metric when both FP and FN matter.
- More informative than Accuracy in many imbalanced classification problems.
- Easy to compare between models.

---

# Disadvantages

- Does not consider True Negatives directly.
- May hide important differences between Precision and Recall.
- Not ideal when one type of error is significantly more costly than the other.
- Does not evaluate the quality of predicted probabilities.
- F1-Score depends on the classification threshold.

---

# Key Points

- F1-Score is the **harmonic mean of Precision and Recall**.
- Formula:

\[
F1 =
2\times
\frac{Precision\times Recall}
{Precision+Recall}
\]

- Direct formula:

\[
F1 =
\frac{2TP}
{2TP+FP+FN}
\]

- F1-Score ranges from **0 to 1**.
- Higher F1-Score is better.
- A high F1-Score requires both Precision and Recall to be reasonably high.
- F1-Score is useful for **imbalanced classification**.
- F1-Score does not directly consider TN.
- Use **Precision** when FP is more costly.
- Use **Recall** when FN is more costly.
- Use **F1-Score** when both FP and FN matter and a balance is required.
- For multiclass problems, use **Macro, Micro, or Weighted F1** according to the evaluation requirement.