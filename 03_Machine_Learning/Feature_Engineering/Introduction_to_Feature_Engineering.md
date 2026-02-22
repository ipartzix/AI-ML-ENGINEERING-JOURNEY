**What is Feature Engineering?**

Feature engineering involves selecting, creating, or transforming features from raw data to make it more suitable for machine learning models. Features, also called dimensions or input variables, are the elements that models use to learn patterns and make predictions. The quality and relevance of features directly impact model accuracy, efficiency, and generalizability.
![alt text](image-1.png)

Feature Engineering is the process of transforming raw data into meaningful and informative features that improve machine learning model performance.

It is one of the most critical steps in the ML pipeline.
---
# Pillar 1: Data Cleaning 
## Objective
Remove noise, inconsistencies, and errors from raw data.

## Key Techniques
- Handling missing values (mean / median / mode / model-based)
- Removing duplicates
- Handling outliers (IQR / Z-score)
- Fixing incorrect data types
- Correcting inconsistent labels

## Example
```python
df['age'].fillna(df['age'].median(), inplace=True)
```
# Pillar 2: Feature Transformation 

Feature Transformation is the process of converting raw data into a format that machine learning algorithms can effectively understand and learn from.

It ensures that features are properly scaled, encoded, and structured for optimal model performance.

---

## 🎯 Objective

- Convert categorical data into numerical format
- Scale numerical features
- Normalize data distributions
- Extract meaningful components from complex data types

---

## 📌 Why Feature Transformation is Important

- Many ML algorithms assume numerical input
- Some models are sensitive to feature scale (e.g., distance-based models)
- Proper transformation improves convergence speed
- Prevents dominance of high-magnitude features

---

# Types of Feature Transformation

---

## Encoding Categorical Variables

Machine learning models cannot process text directly.

### Techniques:
- **One-Hot Encoding**
- **Label Encoding**
- **Ordinal Encoding**
- **Target Encoding**

### Example:
```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df[['category']])