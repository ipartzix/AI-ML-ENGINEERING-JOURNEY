```markdown
# Principal Component Analysis (PCA)

##  Overview
Principal Component Analysis (PCA) is a **feature extraction technique** used to reduce the dimensionality of a dataset while preserving as much important information as possible.

- It helps in handling the **curse of dimensionality**
- Converts **high-dimensional data → low-dimensional data**
- Preserves the **essence (important structure)** of the dataset

---

##  Key Idea
PCA transforms the original features into a new set of features called **Principal Components**.

- These components are:
  - Uncorrelated (orthogonal to each other)
  - Ordered by importance (variance)

---

##  Feature Selection vs Feature Extraction

### Feature Selection
- Selects a subset of original features
- Keeps the most important features
- Based on importance or spread of data

### Feature Extraction (PCA)
- Creates **new features** from existing ones
- These new features are combinations of original features
- Then selects the most important components

---

##  How PCA Works

1. Standardize the dataset (mean = 0, variance = 1)
2. Compute covariance matrix
3. Calculate eigenvalues and eigenvectors
4. Sort eigenvalues in descending order
5. Select top *k* eigenvectors (principal components)
6. Transform data into new lower-dimensional space

---

