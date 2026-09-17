# XGBoost Hyperparameters

## 1. What Are Hyperparameters?

Hyperparameters are settings chosen **before training** that control how the XGBoost model learns.

For the tree-based XGBoost model, the most important hyperparameters are:

- `n_estimators`
- `learning_rate`
- `max_depth`
- `min_child_weight`
- `gamma`
- `subsample`
- `colsample_bytree`
- `reg_alpha`
- `reg_lambda`
- `scale_pos_weight`

XGBoost also provides many additional parameters, but these are the core parameters to understand and tune first.

---

# 2. Core Hyperparameters

## `n_estimators`

**Meaning:** Number of boosting trees.

```python
n_estimators=300
```

### Effect

- Higher → more trees → potentially better learning, but slower training and possible overfitting.
- Lower → faster training, but may underfit.

### Example

```python
n_estimators=100
```

means XGBoost builds 100 boosted trees.

**Think:**  
> How many trees should XGBoost build?

---

## `learning_rate`

Alias: `eta`

**Meaning:** Controls how much each new tree contributes to the final model.

```python
learning_rate=0.05
```

### Effect

- Smaller → slower, more conservative learning.
- Larger → faster learning, but can overfit more easily.

Common values:

```text
0.01
0.03
0.05
0.1
0.2
0.3
```

### Important relationship

Usually:

```text
Lower learning_rate
        ↓
Need more n_estimators
```

For example:

```python
learning_rate=0.05
n_estimators=500
```

**Think:**  
> How strongly should each tree influence the model?

---

## `max_depth`

**Meaning:** Maximum depth of each tree.

```python
max_depth=5
```

### Effect

```text
Low max_depth
    ↓
Simpler trees
    ↓
Less complexity
    ↓
Lower overfitting risk

High max_depth
    ↓
More complex trees
    ↓
Can capture more patterns
    ↓
Higher overfitting risk
```

Common values:

```text
3–10
```

For many tabular datasets, start around:

```python
max_depth=3
```

to

```python
max_depth=6
```

**Think:**  
> How complex can each tree become?

---

## `min_child_weight`

**Meaning:** Minimum sum of instance weight (Hessian) required in a child node before XGBoost allows further partitioning.

```python
min_child_weight=1
```

### Effect

- Lower → easier for trees to create additional splits.
- Higher → more conservative trees.

Common values:

```text
1
3
5
7
10
```

**Think:**  
> How much evidence should a node have before allowing another split?

---

## `gamma`

Alias: `min_split_loss`

**Meaning:** Minimum loss reduction required to make a further split.

```python
gamma=0
```

### Effect

- `gamma=0` → splitting is easier.
- Higher `gamma` → a split must provide more improvement.
- Higher values make the model more conservative.

Common tuning values:

```text
0
0.1
0.5
1
2
5
```

**Think:**  
> How much improvement must a split provide before XGBoost accepts it?

---

# 3. Randomness / Sampling Hyperparameters

## `subsample`

**Meaning:** Fraction of training rows randomly sampled for each boosting iteration.

```python
subsample=0.8
```

means approximately 80% of the training instances are used for each boosting iteration.

### Effect

- `1.0` → use all training rows.
- Lower values → introduce randomness and can help reduce overfitting.
- Too low → may cause underfitting.

Common values:

```text
0.6
0.7
0.8
0.9
1.0
```

**Think:**  
> How many training rows should each tree see?

---

## `colsample_bytree`

**Meaning:** Fraction of features randomly sampled when constructing each tree.

```python
colsample_bytree=0.8
```

means each tree can use approximately 80% of the available features.

### Effect

- `1.0` → all features.
- Lower values → more randomness and potentially less overfitting.
- Too low → important features may be unavailable too often.

Common values:

```text
0.5
0.7
0.8
0.9
1.0
```

**Think:**  
> How many features should each tree see?

---

# 4. Regularization Hyperparameters

Regularization helps control model complexity and overfitting.

## `reg_alpha`

Alias: `alpha`

**Meaning:** L1 regularization on model weights.

```python
reg_alpha=0
```

### Effect

Increasing `reg_alpha` makes the model more conservative.

Common values:

```text
0
0.1
0.5
1
2
5
```

**Think:**  
> How strongly should L1 regularization penalize the model?

---

## `reg_lambda`

Alias: `lambda`

**Meaning:** L2 regularization on model weights.

```python
reg_lambda=1
```

### Effect

Increasing `reg_lambda` makes the model more conservative.

Common values:

```text
1
2
5
10
```

**Think:**  
> How strongly should L2 regularization penalize the model?

---

# 5. Class Imbalance

## `scale_pos_weight`

**Meaning:** Weight applied to the positive class in binary classification.

```python
scale_pos_weight=1
```

This is particularly useful when the classes are highly imbalanced.

A common starting calculation is:

```python
scale_pos_weight = number_of_negative_samples / number_of_positive_samples
```

### Example

Suppose:

```text
Negative = 900
Positive = 100
```

Then:

```python
scale_pos_weight = 900 / 100
# 9.0
```

So:

```python
scale_pos_weight=9
```

may be used as a starting point.

**Important:** Do not automatically use this parameter when the dataset is balanced.

**Think:**  
> How much should the positive class be weighted?

---

# 6. Important Hyperparameter Relationships

## `learning_rate` + `n_estimators`

These should usually be considered together.

### Example A

```python
learning_rate=0.1
n_estimators=300
```

### Example B

```python
learning_rate=0.05
n_estimators=500
```

A smaller learning rate generally requires more boosting rounds.

---

## `max_depth` + `min_child_weight`

Both control tree complexity.

```text
max_depth
    ↓
Maximum tree complexity

min_child_weight
    ↓
Minimum evidence required for further splitting
```

If the model is overfitting, consider making trees more conservative.

---

## `subsample` + `colsample_bytree`

Both introduce randomness.

```text
subsample
    → samples rows

colsample_bytree
    → samples features
```

They can help reduce overfitting.

---

## `reg_alpha` + `reg_lambda`

Both are regularization parameters.

```text
reg_alpha
    → L1 regularization

reg_lambda
    → L2 regularization
```

---

# 7. Quick Reference Table

| Hyperparameter | Controls | Higher value generally means |
|---|---|---|
| `n_estimators` | Number of trees | More boosting rounds |
| `learning_rate` | Contribution of each tree | Faster/stronger updates |
| `max_depth` | Tree depth | More complex trees |
| `min_child_weight` | Minimum child weight | More conservative splitting |
| `gamma` | Minimum split improvement | More conservative splitting |
| `subsample` | Training rows per tree | More rows used |
| `colsample_bytree` | Features per tree | More features used |
| `reg_alpha` | L1 regularization | Stronger L1 penalty |
| `reg_lambda` | L2 regularization | Stronger L2 penalty |
| `scale_pos_weight` | Positive-class weighting | Greater emphasis on positive class |

---

# 8. Good Starting Configuration

For a general classification problem:

```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=5,
    min_child_weight=1,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0,
    reg_lambda=1,
    random_state=42
)
```

This is a **starting point**, not a universally optimal configuration.

---

# 9. Practical Tuning Order

Do not tune every parameter randomly at once.

A clean approach is:

### Step 1 — Tree complexity

Tune:

```python
max_depth
min_child_weight
```

### Step 2 — Split control

Tune:

```python
gamma
```

### Step 3 — Sampling

Tune:

```python
subsample
colsample_bytree
```

### Step 4 — Regularization

Tune:

```python
reg_alpha
reg_lambda
```

### Step 5 — Boosting speed

Tune together:

```python
learning_rate
n_estimators
```

### Step 6 — Class imbalance

If the target is strongly imbalanced, consider:

```python
scale_pos_weight
```

---

# 10. Practical Search Space

A reasonable search space for classification is:

```python
param_grid = {
    "max_depth": [3, 5, 7, 9],
    "min_child_weight": [1, 3, 5, 7],
    "gamma": [0, 0.1, 0.5, 1],
    "subsample": [0.7, 0.8, 0.9, 1.0],
    "colsample_bytree": [0.7, 0.8, 0.9, 1.0],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "reg_alpha": [0, 0.1, 0.5, 1],
    "reg_lambda": [1, 5, 10]
}
```

For a large search space, prefer randomized or Bayesian/Optuna-style optimization instead of trying every possible combination.

---

# 11. CPU-Friendly Configuration

For a CPU-only machine, `hist` is a useful tree construction method:

```python
model = XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=5,
    subsample=0.8,
    colsample_bytree=0.8,
    tree_method="hist",
    random_state=42
)
```

`hist` uses a histogram-based approximate tree-building algorithm and is designed for faster training than the exact method. 

---

# 12. Overfitting Checklist

If:

```text
Training score  → very high
Validation score → much lower
```

the model may be overfitting.

Parameters to consider:

```text
↓ max_depth
↑ min_child_weight
↑ gamma
↓ subsample
↓ colsample_bytree
↑ reg_alpha
↑ reg_lambda
↓ learning_rate
```

Remember that these changes should be validated experimentally rather than applied blindly.

---

# 13. Underfitting Checklist

If both training and validation performance are poor, the model may be underfitting.

Possible directions:

```text
↑ max_depth
↓ min_child_weight
↓ gamma
↑ subsample
↑ colsample_bytree
increase n_estimators
```

Increasing model complexity is not automatically better; always compare validation performance.

---

# 14. Interview Questions

### Q1. What is `n_estimators`?

Number of boosting trees/boosting rounds.

### Q2. What happens when `learning_rate` decreases?

Each tree contributes less, so more trees are generally needed.

### Q3. What does `max_depth` control?

The maximum depth and therefore the complexity of each tree.

### Q4. What does `min_child_weight` do?

It controls the minimum sum of instance weight required in a child node before further partitioning is allowed.

### Q5. What is `gamma`?

The minimum loss reduction required before making a split.

### Q6. Difference between `subsample` and `colsample_bytree`?

```text
subsample
→ samples rows

colsample_bytree
→ samples features
```

### Q7. Difference between `reg_alpha` and `reg_lambda`?

```text
reg_alpha
→ L1 regularization

reg_lambda
→ L2 regularization
```

### Q8. When would you use `scale_pos_weight`?

When dealing with a significantly imbalanced binary classification problem.

### Q9. What happens if `max_depth` is too high?

Trees can become overly complex and the model can overfit.

### Q10. Why combine a low learning rate with more estimators?

Each tree makes a smaller update, so more boosting rounds can be used to build the model gradually.

---

# 15. Mental Model

Remember XGBoost hyperparameters using these questions:

```text
How many trees?
        ↓
n_estimators

How strongly does each tree learn?
        ↓
learning_rate

How complex can each tree become?
        ↓
max_depth

How much evidence is needed for a child node?
        ↓
min_child_weight

How much improvement is needed for a split?
        ↓
gamma

How many rows should each tree see?
        ↓
subsample

How many features should each tree see?
        ↓
colsample_bytree

How much L1 regularization?
        ↓
reg_alpha

How much L2 regularization?
        ↓
reg_lambda

Is the positive class underrepresented?
        ↓
scale_pos_weight
```

---

## Key Takeaway

For learning XGBoost, do **not** try to memorize dozens of parameters.

First master these:

```text
n_estimators
learning_rate
max_depth
min_child_weight
gamma
subsample
colsample_bytree
reg_alpha
reg_lambda
scale_pos_weight
```

The official XGBoost documentation defines these parameters and explains their effects on tree complexity, sampling, regularization, and class weighting. citeturn0search0turn0search2
