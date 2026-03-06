# Feature Scaling – Standardization

Standardization is a feature scaling technique that transforms numerical features so that they have:

- Mean (μ) = 0
- Standard Deviation (σ) = 1

It is also known as **Z-score Normalization**.

---

## Objective

- Center data around zero
- Normalize variance
- Improve model convergence
- Prevent large-scale features from dominating smaller ones

---

## Formula

Z = (X - μ) / σ

Where:

- X = original feature value
- μ = mean of the feature
- σ = standard deviation of the feature

After transformation:

- Mean ≈ 0
- Standard deviation ≈ 1

---

## Why Standardization is Important

Many machine learning algorithms are sensitive to feature scale:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Neural Networks
- Principal Component Analysis (PCA)

Without scaling:

- Gradient descent converges slowly
- Distance-based models become biased
- Features with larger magnitude dominate learning

---

## Example (Manual Calculation)

If:

X = 10  
μ = 8  
σ = 2

Then:

Z = (10 - 8) / 2 = 1

---

## Implementation in Python

### Using scikit-learn

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)