# R² Score (Coefficient of Determination)

## Definition

R² Score (Coefficient of Determination) is a regression evaluation metric that measures how well a regression model explains the variation in the target variable. It indicates the proportion of variance in the dependent variable that is predictable from the independent variables.

The R² Score ranges from **0 to 1**, although it can also be **negative** for poorly performing models.

---

## Formula

\[
R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i-\hat{y_i})^2}{\sum_{i=1}^{n}(y_i-\bar{y})^2}
\]

Where:

- \(y_i\) = Actual value
- \(\hat{y_i}\) = Predicted value
- \(\bar{y}\) = Mean of the actual values
- \(\sum(y_i-\hat{y_i})^2\) = Residual Sum of Squares (RSS)
- \(\sum(y_i-\bar{y})^2\) = Total Sum of Squares (TSS)

---

## Understanding the Formula

### Residual Sum of Squares (RSS)

Measures the unexplained variation (prediction error).

\[
RSS = \sum(y_i-\hat{y_i})^2
\]

Lower RSS indicates better predictions.

---

### Total Sum of Squares (TSS)

Measures the total variation present in the actual data.

\[
TSS = \sum(y_i-\bar{y})^2
\]

---

### R² Calculation

\[
R^2 = 1 - \frac{RSS}{TSS}
\]

If RSS is very small compared to TSS, then R² approaches **1**, indicating an excellent model.

---

## Step-by-Step Example

### Actual Values

```
10, 20, 30, 40
```

### Predicted Values

```
8, 18, 35, 38
```

### Step 1: Calculate the Mean

\[
\bar{y}=\frac{10+20+30+40}{4}=25
\]

---

### Step 2: Calculate RSS

| Actual | Predicted | Squared Error |
|--------|-----------|---------------|
|10|8|4|
|20|18|4|
|30|35|25|
|40|38|4|

\[
RSS = 4+4+25+4 = 37
\]

---

### Step 3: Calculate TSS

| Actual | Mean | Squared Difference |
|--------|------|--------------------|
|10|25|225|
|20|25|25|
|30|25|25|
|40|25|225|

\[
TSS = 225+25+25+225 = 500
\]

---

### Step 4: Calculate R²

\[
R^2 = 1-\frac{37}{500}
\]

\[
R^2 = 1-0.074
\]

\[
R^2 = 0.926
\]

**R² Score = 0.926 (92.6%)**

This means the model explains **92.6% of the variance** in the target variable.

---

## Interpretation

| R² Score | Meaning |
|----------|---------|
| 1.0 | Perfect prediction |
| 0.9 – 1.0 | Excellent fit |
| 0.7 – 0.9 | Good fit |
| 0.5 – 0.7 | Moderate fit |
| 0.0 | Model performs no better than predicting the mean |
| Less than 0 | Worse than predicting the mean |

---

## Advantages

- Easy to interpret.
- Measures how well the model explains data variability.
- Useful for comparing regression models.
- Widely used in regression analysis.

---

## Disadvantages

- Does not indicate whether predictions are unbiased.
- Does not measure prediction error directly.
- Can increase simply by adding more features, even if they are not useful.
- Cannot be used alone to judge model quality.

---

## Adjusted R²

Adjusted R² compensates for adding unnecessary features.

### Formula

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

- \(n\) = Number of observations
- \(p\) = Number of independent features

Adjusted R² only increases when a new feature genuinely improves the model.

---

## Comparison with MAE, MSE and RMSE

| Metric | Measures | Lower is Better? | Unit |
|---------|----------|------------------|------|
| MAE | Average absolute error | Yes | Same as target |
| MSE | Average squared error | Yes | Squared unit |
| RMSE | Root of average squared error | Yes | Same as target |
| R² Score | Explained variance | **Higher is Better** | Unitless |

---

## When to Use R² Score

Use R² when:

- Comparing regression models.
- Measuring how well the model explains the data.
- Reporting regression model performance.
- Evaluating goodness of fit.

Do **not** rely only on R². Always evaluate it alongside MAE, MSE, or RMSE.

---

## Python Example

```python
from sklearn.metrics import r2_score

y_true = [10, 20, 30, 40]
y_pred = [8, 18, 35, 38]

score = r2_score(y_true, y_pred)

print("R² Score:", score)
```

**Output**

```
R² Score: 0.926
```

---

## Key Points

- Used only for **Regression** problems.
- Measures how much variance the model explains.
- Values typically range from **0 to 1**, but can be negative.
- **Higher R² indicates a better model.**
- **R² = 1** means perfect prediction.
- **R² = 0** means the model performs no better than predicting the mean.
- **Negative R²** means the model performs worse than simply predicting the mean.
- Always evaluate R² together with MAE, MSE, or RMSE for a complete assessment of model performance.