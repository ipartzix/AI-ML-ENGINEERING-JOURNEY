# Linear Regression Model — Complete Notes

## 1. Overview
Linear Regression is a **supervised machine learning algorithm** used to model the relationship between a **dependent variable (target)** and one or more **independent variables (features)**.

- Output type: **Continuous (numerical)**
- Goal: Find the **best-fitting line (or hyperplane)**

---

## 2. Types of Linear Regression

### 2.1 Simple Linear Regression
- One input feature

Formula:
y = mx + b

Where:
- y = predicted output
- x = input feature
- m = slope (weight)
- b = intercept (bias)

---

### 2.2 Multiple Linear Regression
- Multiple input features

Formula:
y = β0 + β1x1 + β2x2 + ... + βnxn

Where:
- β0 = intercept
- β1, β2, ..., βn = coefficients

---

## 3. Hypothesis Function

General form:
h(x) = θ0 + θ1x1 + θ2x2 + ... + θnxn

Matrix form:
h(X) = Xθ

---

## 4. Cost Function (Loss Function)

Mean Squared Error (MSE):

J(θ) = (1/n) * Σ(yi - ŷi)^2

- yi = actual value
- ŷi = predicted value
- n = number of samples

Objective:
Minimize J(θ)

---

## 5. Training Methods

### 5.1 Gradient Descent

Update rule:
θj = θj - α * (∂J/∂θj)

Where:
- α = learning rate
- ∂J/∂θj = gradient

Steps:
1. Initialize parameters
2. Compute predictions
3. Calculate error
4. Update parameters
5. Repeat until convergence

---

### 5.2 Normal Equation (Closed Form)

θ = (XᵀX)^(-1) Xᵀy

- No iteration required
- Computationally expensive for large datasets

---

## 6. Assumptions of Linear Regression

1. Linearity → Relationship between X and y is linear  
2. Independence → Observations are independent  
3. Homoscedasticity → Constant variance of errors  
4. Normality → Errors are normally distributed  
5. No Multicollinearity → Features are not highly correlated  

---

## 7. Evaluation Metrics

### 7.1 Mean Absolute Error (MAE)
MAE = (1/n) * Σ|yi - ŷi|

### 7.2 Mean Squared Error (MSE)
MSE = (1/n) * Σ(yi - ŷi)^2

### 7.3 Root Mean Squared Error (RMSE)
RMSE = √MSE

### 7.4 R² Score (Coefficient of Determination)
R² = 1 - (SS_res / SS_tot)

---

## 8. Advantages

- Simple and easy to understand  
- Fast training  
- Interpretable coefficients  
- Works well for linear relationships  

---

## 9. Disadvantages

- Cannot model non-linear relationships  
- Sensitive to outliers  
- Assumes strict statistical conditions  
- Poor performance with high multicollinearity  

---

## 10. Regularization in Linear Regression

### 10.1 Ridge Regression (L2 Regularization)
Adds penalty:
λ * Σθ²

### 10.2 Lasso Regression (L1 Regularization)
Adds penalty:
λ * Σ|θ|

### 10.3 ElasticNet
Combination of L1 and L2

---

## 11. Feature Engineering Considerations

- Feature scaling (important for gradient descent)
- Handling missing values
- Removing multicollinearity
- Polynomial features for non-linearity
