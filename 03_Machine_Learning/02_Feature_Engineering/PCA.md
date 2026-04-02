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

##  Important Concepts

### 1. Curse of Dimensionality
- As dimensions increase:
  - Data becomes sparse
  - Models become complex
  - Performance decreases
- PCA reduces dimensions to solve this issue

---

### 2. Variance
- Variance measures the **spread of data**
- PCA tries to **maximize variance**
- Higher variance = more information

 PCA selects directions (axes) where:
- Data varies the most
- Information is preserved

---

### 3. New Coordinate System
- PCA finds new axes (principal components)
- These axes:
  - Are rotated versions of original axes
  - Capture maximum variance

---

##  Why PCA Works

- Variance helps differentiate data points
- By keeping high-variance directions:
  - PCA preserves relationships between data points
- Reduces noise and redundancy

---

##  Summary Points

- PCA is a **feature extraction technique**
- Reduces dimensionality
- Solves **curse of dimensionality**
- Creates **new features (principal components)**
- Maximizes **variance**
- Preserves important structure of data

---

##  Limitations

- PCA is linear (cannot capture complex nonlinear patterns)
- Interpretation of new features is difficult
- Sensitive to scaling (requires normalization)

---

##  Use Cases

- Data visualization (2D/3D projection)
- Noise reduction
- Preprocessing for ML models
- Compression of large datasets

---

##  One-Line Definition
> PCA transforms high-dimensional data into a lower-dimensional space by creating new features that maximize variance while preserving data structure.
```
###  Summary Flow

```
Raw Data
↓
Standardization
↓
Covariance Matrix
↓
Eigenvalues & Eigenvectors
↓
Select Top k Components
↓
Project Data
↓
Reduced Dataset
```

---

## 12. Key Takeaway

PCA transforms data into a new coordinate system where:
- First axis = maximum variance
- Second axis = next maximum (orthogonal)
- And so on...

This helps simplify complex datasets while retaining essential structure.
## 3. Step-by-Step Solution (Numerical Example)
### Step 0: Example Dataset

Consider:

\[
X =
\begin{bmatrix}
2 & 4 \\
4 & 2 \\
6 & 8 \\
8 & 6
\end{bmatrix}
\]

---

### Step 1: Mean Centering

Compute mean of each column:

\[
\mu = [5, 5]
\]

Subtract mean:

\[
X_{centered} =
\begin{bmatrix}
-3 & -1 \\
-1 & -3 \\
1 & 3 \\
3 & 1
\end{bmatrix}
\]

---

### Step 2: Covariance Matrix

\[
C = \frac{1}{n-1} X^T X
\]

\[
C =
\begin{bmatrix}
6.67 & 4 \\
4 & 6.67
\end{bmatrix}
\]

---

### Step 3: Eigenvalues & Eigenvectors

Solve:

\[
|C - \lambda I| = 0
\]

Eigenvalues:

\[
\lambda_1 = 10.67,\quad \lambda_2 = 2.67
\]

Eigenvectors:

\[
v_1 =
\begin{bmatrix}
0.707 \\
0.707
\end{bmatrix}, \quad
v_2 =
\begin{bmatrix}
-0.707 \\
0.707
\end{bmatrix}
\]

---

