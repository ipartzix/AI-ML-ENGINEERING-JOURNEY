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
