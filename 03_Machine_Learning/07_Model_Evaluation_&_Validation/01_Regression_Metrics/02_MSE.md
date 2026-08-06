# Mean Squared Error (MSE)

## Definition

Mean Squared Error (MSE) is a regression evaluation metric that measures the average of the squared differences between the actual values and the predicted values. Squaring the errors gives greater weight to larger errors, making MSE highly sensitive to outliers.

## Formula

\[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2
\]

Where:

- \(n\) = Number of observations
- \(y_i\) = Actual value
- \(\hat{y_i}\) = Predicted value
- \((y_i-\hat{y_i})^2\) = Squared error

---

## Step-by-Step Example

| Actual (\(y\)) | Predicted (\(\hat{y}\)) | Error | Squared Error |
|----------------|--------------------------|-------|---------------|
| 10 | 8 | 2 | 4 |
| 20 | 18 | 2 | 4 |
| 30 | 35 | -5 | 25 |
| 40 | 38 | 2 | 4 |

Total Squared Error

\[
4 + 4 + 25 + 4 = 37
\]

Number of observations

\[
n = 4
\]

Therefore,

\[
MSE = \frac{37}{4} = 9.25
\]

**Mean Squared Error = 9.25**

---

## Interpretation

- **MSE = 0** → Perfect prediction.
- **Lower MSE** → Better model performance.
- **Higher MSE** → Larger prediction errors.

Since the errors are squared, **large prediction mistakes receive much larger penalties than small mistakes**.

---

## Advantages

- Penalizes large errors more heavily.
- Smooth and differentiable, making it suitable for optimization algorithms like Gradient Descent.
- Widely used as the default loss function for Linear Regression.
- Easy to compute.

---

## Disadvantages

- Highly sensitive to outliers.
- The unit of MSE is the **square of the target variable**, making it less interpretable.
- Large errors dominate the metric.

---

## Comparison with MAE

| MSE | MAE |
|-----|-----|
| Uses squared error | Uses absolute error |
| Highly sensitive to outliers | Less sensitive to outliers |
| Penalizes large errors heavily | Treats all errors equally |
| Squared unit of target | Same unit as target |
| Commonly used as a loss function | Commonly used as an evaluation metric |

---

## When to Use MSE

Use MSE when:

- Large prediction errors should be penalized heavily.
- Training regression models using Gradient Descent.
- Outliers are important and should significantly influence the model.
- You need a smooth, differentiable loss function for optimization.

---

## Python Example

```python
from sklearn.metrics import mean_squared_error

y_true = [10, 20, 30, 40]
y_pred = [8, 18, 35, 38]

mse = mean_squared_error(y_true, y_pred)

print("MSE:", mse)
```

**Output**

```
MSE: 9.25
```

---

## Key Points

- Used only for **Regression** problems.
- Lower MSE indicates a better model.
- Errors are squared before averaging.
- Large prediction errors are penalized more than small ones.
- Highly sensitive to outliers.
- Unit of MSE is the **square of the target variable**.
- RMSE is obtained by taking the square root of MSE.