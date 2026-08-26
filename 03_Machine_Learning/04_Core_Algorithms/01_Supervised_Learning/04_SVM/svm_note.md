# Support Vector Machine (SVM)

## 1. What is SVM?
- Supervised learning algorithm
- Used mainly for classification
- Can also be used for regression (SVR)
- Finds the optimal decision boundary (hyperplane)

## 2. Core Concepts
- Hyperplane
- Margin
- Support Vectors
- Decision Boundary
- Maximum Margin Classifier
- Hard Margin vs Soft Margin

## 3. Linear SVM
- Linear decision boundary
- Hinge Loss
- Regularization parameter (C)
- Objective function
- Classification intuition

## 4. Kernel SVM
- Used for non-linearly separable data
- Kernel Trick
- Common kernels:
  - Linear
  - Polynomial
  - RBF (Gaussian)
  - Sigmoid
- Kernel parameters:
  - C
  - Gamma
  - Degree (Polynomial)

## 5. SVM for Regression
- Support Vector Regression (SVR)
- ε-insensitive loss
- Basic intuition

## 6. Important Hyperparameters
- C
- kernel
- gamma
- degree

## 7. Advantages
- Effective in high-dimensional spaces
- Works well with clear margins
- Kernel trick handles non-linear boundaries

## 8. Limitations
- Can be slow on large datasets
- Sensitive to feature scaling
- Hyperparameter tuning can be important

## 9. SVM with Scikit-learn
- SVC
- SVR
- LinearSVC

## 10. Interview Points
- Why maximize the margin?
- What are support vectors?
- Hard margin vs soft margin
- Role of C
- What is the kernel trick?
- C vs gamma
- Linear SVM vs Kernel SVM