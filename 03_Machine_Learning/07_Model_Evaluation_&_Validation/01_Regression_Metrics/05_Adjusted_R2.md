# Adjusted R² Score

## Definition

Adjusted R² is a modified version of the R² Score that adjusts for the number of independent features (predictors) in a regression model. Unlike R², which always stays the same or increases when new features are added, Adjusted R² increases only if the new feature improves the model significantly.

It helps determine whether additional features genuinely improve the model or simply make it more complex.

---

## Formula

\[
Adjusted\ R^2
=
1-
\left(
\frac{(1-R^2)(n-1)}
{n-p-1}
\right)
\]

Where:

- \(R^2\) = R² Score
- \(n\) = Number of observations
- \(p\) = Number of independent features (predictors)

---

## Why Do We Need Adjusted R²?

Suppose you have a regression model with:

- 3 useful features
- R² = 0.85

Now you add 10 random, unrelated features.

The R² Score may increase slightly because adding more features almost never decreases R².

However, those extra features do not actually improve prediction.

Adjusted R² penalizes unnecessary features, helping identify whether the added complexity is justified.

---

## Step-by-Step Example

Suppose:

- Number of observations

\[
n = 100
\]

- Number of features

\[
p = 5
\]

- R² Score

\[
R^2 = 0.92
\]

### Step 1: Substitute the values

\[
Adjusted\ R^2
=
1-
\frac{(1-0.92)(100-1)}
{100-5-1}
\]

### Step 2: Simplify

\[
=
1-
\frac{0.08\times99}{94}
\]

\[
=
1-
0.0843
\]

### Step 3: Final Answer

\[
Adjusted\ R^2
=
0.9157
\]

**Adjusted R² ≈ 0.916**

Notice that the Adjusted R² is slightly lower than the R² Score because it accounts for the number of predictors.

---

## Interpretation

| Adjusted R² | Meaning |
|-------------|---------|
| 1.0 | Perfect model |
| Close to 1 | Excellent fit |
| Close to 0 | Weak explanatory power |
| Negative | Model performs worse than predicting the mean |

---

## Difference Between R² and Adjusted R²

| R² Score | Adjusted R² |
|-----------|-------------|
| Measures explained variance | Measures explained variance while considering the number of features |
| Always increases or stays the same when features are added | Can increase or decrease when features are added |
| Does not penalize unnecessary predictors | Penalizes unnecessary predictors |
| Best for simple regression | Better for multiple linear regression |

---

## Advantages

- Prevents overfitting by penalizing unnecessary features.
- Better metric for comparing multiple regression models.
- Indicates whether newly added features improve the model.
- More reliable than R² when using multiple predictors.

---

## Disadvantages

- Slightly more difficult to understand than R².
- Not suitable for comparing models trained on different datasets.
- Does not measure prediction error directly.

---

## When to Use Adjusted R²

Use Adjusted R² when:

- Building **Multiple Linear Regression** models.
- Comparing models with different numbers of predictors.
- Performing feature selection.
- Detecting overfitting caused by unnecessary features.

---

## Comparison with Other Regression Metrics

| Metric | Measures | Better Value |
|---------|----------|--------------|
| MAE | Average absolute error | Lower |
| MSE | Average squared error | Lower |
| RMSE | Root mean squared error | Lower |
| R² Score | Explained variance | Higher |
| Adjusted R² | Explained variance with feature penalty | Higher |

---

## Python Example

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

import numpy as np

# Sample data
X = np.array([
    [1, 2],
    [2, 1],
    [3, 4],
    [4, 3],
    [5, 5]
])

y = np.array([5, 6, 9, 10, 12])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

r2 = r2_score(y, y_pred)

n = len(y)
p = X.shape[1]

adjusted_r2 = 1 - ((1 - r2) * (n - 1)) / (n - p - 1)

print("R² Score:", r2)
print("Adjusted R²:", adjusted_r2)
```

---

## Key Points

- Used only for **Regression** problems.
- Modified version of the R² Score.
- Penalizes unnecessary predictors.
- Preferred over R² for **Multiple Linear Regression**.
- Can increase or decrease when new features are added.
- Helps detect overfitting.
- Always compare models using Adjusted R² when they contain different numbers of features.