# Mean Absolute Error (MAE)

## Definition

Mean Absolute Error (MAE) is a regression evaluation metric that measures the average magnitude of errors between the actual values and the predicted values. It treats all errors equally by taking the absolute value of each error.

## Formula

\[
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y_i}|
\]

Where:

- \(n\) = Number of observations
- \(y_i\) = Actual value
- \(\hat{y_i}\) = Predicted value
- \(|y_i-\hat{y_i}|\) = Absolute error

---

## Step-by-Step Example

| Actual (\(y\)) | Predicted (\(\hat{y}\)) | Absolute Error |
|----------------|--------------------------|----------------|
| 10             | 8                        | 2              |
| 20             | 18                       | 2              |
| 30             | 35                       | 5              |
| 40             | 38                       | 2              |

Total Absolute Error

\[
2 + 2 + 5 + 2 = 11
\]

Number of observations

\[
n = 4
\]

Therefore,

\[
MAE = \frac{11}{4} = 2.75
\]

**Mean Absolute Error = 2.75**

---

## Interpretation

- **MAE = 0** → Perfect prediction.
- **Lower MAE** → Better model performance.
- **Higher MAE** → Larger prediction errors.

MAE is expressed in the **same unit as the target variable**.

Example:
- House price prediction → MAE = ₹50,000 means the model is wrong by about ₹50,000 on average.
- Temperature prediction → MAE = 2°C means predictions are off by approximately 2°C.

---

## Advantages

- Easy to understand and interpret.
- Same unit as the target variable.
- Less sensitive to outliers than MSE.
- Every error contributes equally.

---

## Disadvantages

- Does not penalize large errors more heavily.
- Not differentiable at zero (mainly important during optimization).
- Large mistakes and small mistakes are weighted equally.

---

## Comparison with MSE

| MAE | MSE |
|-----|-----|
| Uses absolute error | Uses squared error |
| Less sensitive to outliers | Highly sensitive to outliers |
| Easy to interpret | Harder to interpret because errors are squared |
| Same unit as target | Squared unit of target |

---

## When to Use MAE

Use MAE when:
- Every prediction error should have equal importance.
- The dataset contains outliers and you don't want them to dominate the metric.
- You want an easily interpretable regression metric.

---

## Python Example

```python
from sklearn.metrics import mean_absolute_error

y_true = [10, 20, 30, 40]
y_pred = [8, 18, 35, 38]

mae = mean_absolute_error(y_true, y_pred)

print("MAE:", mae)
```

**Output**

```
MAE: 2.75
```

---

## Key Points

- Used only for **Regression** problems.
- Lower MAE indicates a better model.
- MAE measures the average absolute prediction error.
- Errors are not squared, so all mistakes are treated equally.
- MAE is measured in the same units as the target variable.