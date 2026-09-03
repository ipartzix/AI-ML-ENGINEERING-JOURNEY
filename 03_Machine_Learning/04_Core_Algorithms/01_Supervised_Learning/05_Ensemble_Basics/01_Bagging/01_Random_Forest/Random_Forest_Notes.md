# Random Forest

## 1. What is Random Forest?

**Random Forest** is an ensemble learning algorithm that combines multiple **Decision Trees** to produce a stronger and more stable model.

It can be used for:

- Classification
- Regression

The main idea is:

> Build many different decision trees and combine their predictions.

Random Forest is based on the **Bagging** idea, but it adds an additional source of randomness: **random feature selection**.

---

## 2. Why Random Forest?

A single Decision Tree can easily **overfit** the training data.

For example:

```text
Training Data
     │
     ├── Decision Tree 1 → Prediction
     │
     ├── Decision Tree 2 → Prediction
     │
     ├── Decision Tree 3 → Prediction
     │
     ├── ...
     │
     └── Decision Tree N → Prediction
                  │
                  ▼
          Combine Predictions
                  │
                  ▼
              Final Result
```

By combining many trees, Random Forest generally:

- Reduces variance
- Reduces overfitting
- Improves generalization
- Produces more stable predictions

---

# 3. How Random Forest Works

Random Forest introduces randomness in **two major ways**.

### Step 1: Bootstrap Sampling

For every tree, Random Forest creates a different training dataset by sampling from the original dataset **with replacement**.

Example:

```text
Original Dataset:
A B C D E F G H

Tree 1:
A B B D F G H H

Tree 2:
A C C D E G G H

Tree 3:
B B C E F F H H
```

Because sampling is performed with replacement:

- A sample can appear multiple times.
- Some samples may not appear in a particular tree's training set.

This is called a **bootstrap sample**.

---

### Step 2: Random Feature Selection

At each split of a decision tree, Random Forest considers only a **random subset of features** instead of considering all features.

Example:

```text
Features:
Age
Salary
Experience
Education
Location
Credit Score

Random subset for one split:
Salary
Experience
Credit Score
```

This makes the trees less correlated with each other.

---

### Step 3: Build Many Decision Trees

Each tree is trained using:

1. A different bootstrap sample
2. Random subsets of features at each split

The result is a collection of diverse decision trees.

```text
             Random Forest
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
    Tree 1      Tree 2       Tree 3
       │           │           │
       ▼           ▼           ▼
      Yes          No          Yes
       │           │           │
       └───────────┼───────────┘
                   ▼
              Final Prediction
```

---

# 4. Final Prediction

## Classification

For classification, Random Forest normally uses **majority voting**.

Example:

```text
Tree 1 → Cat
Tree 2 → Dog
Tree 3 → Cat
Tree 4 → Cat
Tree 5 → Dog
```

Votes:

```text
Cat → 3
Dog → 2
```

Final prediction:

```text
Cat
```

### Formula

For classification:

\[
\hat{y} = mode(T_1(x), T_2(x), ..., T_n(x))
\]

where:

- \(T_i(x)\) = prediction from tree \(i\)
- \(mode\) = most frequent prediction

---

# 5. Random Forest Regression

For regression, Random Forest combines the predictions by taking their **average**.

Example:

```text
Tree 1 → 100
Tree 2 → 110
Tree 3 → 105
Tree 4 → 115
Tree 5 → 120
```

Final prediction:

\[
\frac{100+110+105+115+120}{5}=110
\]

So:

```text
Final Prediction = 110
```

---

# 6. Random Forest vs Decision Tree

| Feature | Decision Tree | Random Forest |
|---|---|---|
| Number of trees | One | Many |
| Bootstrap sampling | No | Yes |
| Random feature selection | No | Yes |
| Overfitting | Higher | Lower |
| Variance | High | Lower |
| Stability | Lower | Higher |
| Interpretability | Easy | More difficult |
| Training time | Faster | Slower |
| Prediction time | Faster | Slower |
| Accuracy | Often lower | Often higher |

### Simple idea

```text
Decision Tree:
One expert → Final answer

Random Forest:
Many experts → Vote/Average → Final answer
```

---

# 7. Bagging

**Bagging** stands for:

> **Bootstrap Aggregating**

Bagging is an ensemble technique that:

1. Creates multiple bootstrap samples.
2. Trains a separate model on each sample.
3. Combines their predictions.

For classification:

```text
Majority Voting
```

For regression:

```text
Average
```

The purpose of Bagging is mainly to **reduce variance** and make the model more stable.

---

# 8. Bagging vs Random Forest

Random Forest is closely related to Bagging.

The key difference is:

> **Random Forest = Bagging + Random Feature Selection**

| Feature | Bagging | Random Forest |
|---|---|---|
| Ensemble technique | Yes | Yes |
| Bootstrap samples | Yes | Yes |
| Multiple models | Yes | Yes |
| Usually uses Decision Trees | Often | Yes |
| Random feature selection at each split | Not necessarily | Yes |
| Main source of diversity | Different training samples | Different samples + different features |
| Correlation between trees | Can be higher | Usually lower |
| Overfitting control | Good | Generally better for tree ensembles |
| Variance reduction | Yes | Yes |
| Classification | Yes | Yes |
| Regression | Yes | Yes |

### Important distinction

Suppose the dataset has:

```text
Feature 1
Feature 2
Feature 3
Feature 4
Feature 5
```

**Bagging with Decision Trees:**

```text
Bootstrap Dataset
      │
      ├── Tree 1 → considers all available features at splits
      ├── Tree 2 → considers all available features at splits
      └── Tree 3 → considers all available features at splits
```

**Random Forest:**

```text
Bootstrap Dataset
      │
      ├── Tree 1 → random feature subsets
      ├── Tree 2 → different random feature subsets
      └── Tree 3 → different random feature subsets
```

Therefore, Random Forest creates more diversity among trees.

---

# 9. Why Random Feature Selection Matters

Suppose one feature is extremely strong.

Without feature randomness, many decision trees may repeatedly choose that same feature for their important splits.

The trees can then become highly similar.

Highly similar trees provide less benefit from averaging because their errors are correlated.

Random Forest reduces this correlation by forcing each split to consider only a random subset of features.

### Key idea

```text
Less correlation between trees
            ↓
More diverse trees
            ↓
Better ensemble
            ↓
Lower variance
```

---

# 10. Bias and Variance

Random Forest is particularly effective for reducing **variance**.

A single deep Decision Tree can have:

```text
Low Bias
High Variance
```

Random Forest combines many trees:

```text
Many high-variance trees
          ↓
      Averaging
          ↓
Lower variance
```

The trees do not need to be individually perfect.

They need to be **different enough** so that their errors can partially cancel out.

---

# 11. Out-of-Bag (OOB) Samples

Because bootstrap sampling is performed with replacement, each tree does not necessarily use every training sample.

The samples that are not selected for a particular tree are called **Out-of-Bag (OOB) samples**.

Example:

```text
Original:
A B C D E F G H

Bootstrap sample:
A B B D F G H H

OOB samples:
C E
```

OOB samples can be used to estimate model performance without requiring a separate validation set in the same way.

In scikit-learn:

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    oob_score=True,
    random_state=42
)

model.fit(X_train, y_train)

print(model.oob_score_)
```

---

# 12. Important Random Forest Hyperparameters

## `n_estimators`

Number of trees in the forest.

```python
RandomForestClassifier(n_estimators=100)
```

Higher values generally provide a more stable estimate, but increase computation.

---

## `max_depth`

Maximum depth of each tree.

```python
RandomForestClassifier(max_depth=10)
```

Smaller depth:

- Simpler trees
- Lower complexity
- Can increase bias

Larger depth:

- More complex trees
- Can reduce bias
- Individual trees can overfit

---

## `max_features`

Number or proportion of features considered when searching for the best split.

```python
RandomForestClassifier(max_features="sqrt")
```

This parameter is particularly important because random feature selection is a core part of Random Forest.

---

## `min_samples_split`

Minimum number of samples required to split an internal node.

```python
RandomForestClassifier(min_samples_split=5)
```

---

## `min_samples_leaf`

Minimum number of samples required to be at a leaf node.

```python
RandomForestClassifier(min_samples_leaf=2)
```

---

## `bootstrap`

Whether bootstrap samples are used.

```python
RandomForestClassifier(bootstrap=True)
```

---

## `random_state`

Controls reproducibility.

```python
RandomForestClassifier(random_state=42)
```

---

# 13. Random Forest Classification Example

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

---

# 14. Random Forest Regression Example

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

---

# 15. Advantages of Random Forest

### 1. Reduces Overfitting

Compared with a single decision tree, combining many diverse trees usually improves generalization.

### 2. Handles Non-Linear Relationships

Random Forest can model complex non-linear relationships between features and the target.

### 3. Works for Classification and Regression

```text
RandomForestClassifier
RandomForestRegressor
```

### 4. Handles Feature Interactions

It can automatically capture interactions between features.

### 5. Less Sensitive to Feature Scaling

Tree-based models generally do not require feature scaling.

For example:

```text
StandardScaler
MinMaxScaler
```

are usually not necessary for Random Forest.

### 6. Provides Feature Importance

Random Forest can provide information about feature importance.

```python
model.feature_importances_
```

---

# 16. Disadvantages of Random Forest

### 1. Computationally More Expensive

Many trees require more:

- CPU
- RAM
- Training time
- Prediction time

than a single Decision Tree.

### 2. Less Interpretable

Understanding one tree is relatively easy.

Understanding hundreds of trees is much harder.

### 3. Large Model Size

A forest containing hundreds or thousands of trees can consume significant memory.

### 4. Can Still Overfit

Random Forest is resistant to overfitting, but it is not impossible to overfit.

Hyperparameters still need to be selected appropriately.

---

# 17. Do We Need Feature Scaling?

Usually **No**.

Random Forest uses decision-tree-based splits such as:

```text
Feature < threshold
```

The relative ordering of values matters more than their scale.

Therefore, this is generally unnecessary:

```python
from sklearn.preprocessing import StandardScaler
```

For example:

```text
Age:       20 - 60
Salary:    20,000 - 200,000
```

Random Forest can generally work directly with these values.

---

# 18. Random Forest Feature Importance

Random Forest can estimate how useful each feature is for making predictions.

Example:

```python
import pandas as pd

importance = pd.Series(
    model.feature_importances_,
    index=X_train.columns
)

print(importance.sort_values(ascending=False))
```

Example output:

```text
Temperature      0.42
Humidity         0.31
Soil Moisture    0.19
Rainfall         0.08
```

A higher importance score indicates that the feature contributed more according to that importance calculation.

**Important:** Feature importance should not automatically be interpreted as causal importance.

---

# 19. Random Forest Mental Model

Remember Random Forest as:

```text
                RANDOM FOREST
                     │
        ┌────────────┴────────────┐
        │                         │
Bootstrap Sampling       Random Feature Selection
        │                         │
        └────────────┬────────────┘
                     │
              Many Decision Trees
                     │
                     ▼
              Combine Predictions
                     │
              ┌──────┴──────┐
              ▼             ▼
       Classification    Regression
          Voting           Average
```

---

# 20. Key Formula

For a classification problem:

\[
\hat{y} = mode\{T_1(x),T_2(x),...,T_B(x)\}
\]

For regression:

\[
\hat{y} = \frac{1}{B}\sum_{b=1}^{B}T_b(x)
\]

where:

- \(B\) = number of trees
- \(T_b(x)\) = prediction from tree \(b\)
- \(x\) = input features

---

# 21. Random Forest vs Bagging — One-Line Interview Answer

> **Bagging trains multiple models on bootstrap samples and aggregates their predictions, while Random Forest is a specialized tree-based ensemble that combines bootstrap sampling with random feature selection at each split.**

---

# 22. Important Interview Points

Remember these points:

1. Random Forest is an **ensemble learning algorithm**.
2. It consists of multiple **Decision Trees**.
3. It uses **bootstrap sampling**.
4. It uses **random feature selection** at each split.
5. Classification uses **majority voting**.
6. Regression uses **averaging**.
7. It mainly reduces **variance**.
8. It reduces correlation between trees through feature randomness.
9. OOB samples can be used for an internal performance estimate.
10. Feature scaling is generally unnecessary.
11. `n_estimators` controls the number of trees.
12. `max_depth` controls tree depth.
13. `max_features` controls the number of features considered at a split.
14. Random Forest can be used for both classification and regression.
15. **Random Forest = Bagging + Random Feature Selection**.

---

# 23. Quick Revision

```text
Decision Tree
    ↓
One tree
    ↓
Can overfit

Bagging
    ↓
Bootstrap samples
    ↓
Multiple models
    ↓
Aggregate predictions
    ↓
Reduce variance

Random Forest
    ↓
Bootstrap samples
    +
Random feature selection
    ↓
Multiple Decision Trees
    ↓
Voting / Averaging
    ↓
Lower variance + better generalization
```

## Final Concept

> **Random Forest builds many diverse Decision Trees using bootstrap samples and random subsets of features, then combines their predictions to obtain a more robust and generalizable model.**
