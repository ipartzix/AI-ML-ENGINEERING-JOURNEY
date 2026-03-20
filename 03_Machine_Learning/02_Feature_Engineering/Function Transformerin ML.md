# Feature Transformation Techniques (Machine Learning Notes)

Feature transformation is used to improve model performance by making data more suitable for learning algorithms. Below are some important transformations:

---

## 🔹 1. Function Transformer

###  Definition
A **Function Transformer** applies a custom mathematical function to features.

###  Usage
- Useful when you want full control over transformation.
- Can apply `log`, `sqrt`, `reciprocal`, or any custom function.

###  Example (Python)
```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

transformer = FunctionTransformer(np.log1p)  # log(1 + x)
X_transformed = transformer.fit_transform(X)


#  Feature Transformation Notes

## 🔹 2. Log Transformation

### 📌 Formula
X' = log(X)

### 📌 When to Use
- Reduces right-skewed data  
- Handles large outliers  
- Converts multiplicative relationships → additive  

### 📌 Important Notes
- Works only for positive values  
- Use log1p(x) if zeros are present  

### 📌 Example
```python
import numpy as np

X_log = np.log1p(X)