# Root Mean Squared Error (RMSE)

## Definition

Root Mean Squared Error (RMSE) is a regression evaluation metric that measures the average magnitude of prediction errors by taking the square root of the Mean Squared Error (MSE). It gives higher importance to large errors while expressing the result in the same unit as the target variable.

## Formula

\[
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2}
\]

Where:

- \(n\) = Number of observations
- \(y_i\) = Actual value
- \(\hat{y_i}\) = Predicted value
- \((y_i-\hat{y_i})^2\) = Squared error

---

## Relationship with MSE

RMSE is simply the square root of MSE.

\[
RMSE = \sqrt{MSE}
\]

Example:

If

\[
MSE = 9.25
\]

Then

\[
RMSE = \sqrt{9.25} \approx 3.04
\]

---

## Step-by-Step Example

| Actual (\(y\)) | Predicted (\(\hat{y}\)) | Error | Squared Error |
|----------------|--------------------------|-------|---------------|
| 10 | 8 | 2 | 4 |
| 20 | 18 | 2 | 4 |
| 30 | 35 | -5 | 25 |
| 40 | 38 | 2 | 4 |

### Step 1: Calculate MSE

Total Squared Error

\[
4 + 4 + 25 + 4 = 37
\]

\[
MSE = \frac{37}{4} = 9.25
\]

### Step 2: Calculate RMSE

\[
RMSE = \sqrt{9.25} \approx 3.04
\]

**Root Mean Squared Error = 3.04**

---

## Interpretation

- **RMSE = 0** → Perfect prediction.
- **Lower RMSE** → Better model performance.
- **Higher RMSE** → Larger prediction errors.

Unlike MSE, RMSE is expressed in the **same unit as the target variable**, making it easier to interpret.

Example:

- House price prediction → RMSE = ₹50,000 means predictions are off by approximately ₹50,000.
- Temperature prediction → RMSE = 2°C means predictions are off by about 2°C.

---

## Advantages

- Same unit as the target variable.
- Penalizes large errors more than small ones.
- Easy to interpret compared to MSE.
- Widely used for evaluating regression models.

---

## Disadvantages

- Sensitive to outliers.
- Large prediction errors have a significant impact.
- Requires an additional square root computation compared to MSE.

---

## Comparison with MAE and MSE

| Metric | Error Used | Outlier Sensitivity | Unit |
|--------|------------|---------------------|------|
| MAE | Absolute Error | Low | Same as target |
| MSE | Squared Error | High | Squared unit |
| RMSE | Square Root of Squared Error | High | Same as target |

---

## When to Use RMSE

Use RMSE when:

- Large prediction errors should be penalized.
- You want an interpretable metric in the original unit of the target variable.
- Comparing regression models.
- Evaluating models where large errors are costly.

---

## Python Example

```python
from sklearn.metrics import root_mean_squared_error

y_true = [10, 20, 30, 40]
y_pred = [8, 18, 35, 38]

rmse = root_mean_squared_error(y_true, y_pred)

print("RMSE:", rmse)
```

**Output**

```
RMSE: 3.041381265
```

> **Note:** For older versions of scikit-learn, use:

```python
from sklearn.metrics import mean_squared_error
import numpy as np

rmse = np.sqrt(mean_squared_error(y_true, y_pred))
```

---

## Key Points

- Used only for **Regression** problems.
- RMSE is the square root of MSE.
- Lower RMSE indicates a better model.
- Penalizes large prediction errors more heavily.
- Same unit as the target variable, making interpretation easier.
- More sensitive to outliers than MAE.
- One of the most commonly reported regression evaluation metrics.