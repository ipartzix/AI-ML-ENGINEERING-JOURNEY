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
