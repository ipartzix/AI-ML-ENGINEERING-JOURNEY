# Comprehensive Guide to Decision Tree Hyperparameters

A Decision Tree recursively splits data into smaller subsets until a stopping criterion is met. The goal is to create partitions that maximize the homogeneity of the target variable in each subset.

---

## 🚀 Basic Implementation (Classification)

This simple implementation trains a Decision Tree classifier on the Iris dataset and evaluates its accuracy using Scikit-Learn.

```python
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

---

## 🧠 Core Machine Learning Concepts

### 1. Entropy and Information Gain
* **Entropy**: Measures the impurity or randomness in a dataset. Lower entropy means higher purity.
* **Information Gain**: Calculates the reduction in entropy after a dataset is split. The feature yielding the highest Information Gain is selected for the split.

### 2. Gini Impurity
* An alternative to entropy, Gini Impurity measures the probability of incorrectly classifying a randomly chosen element from the subset. A lower Gini value indicates a purer split.

### 3. Overfitting vs. Underfitting
* **Overfitting**: Occurs when the model learns noise and specific details from the training data, leading to poor generalization on unseen data.
* **Underfitting**: Occurs when the model is too simple to capture the underlying patterns within the data.

---

## 🛠️ Hyperparameter Tuning Matrix

Hyperparameters are explicitly configured before training to balance complexity and mitigate overfitting or underfitting.

### 1. Structural Parameters

```python
# Max Depth: Limits how deep the tree can grow. 
# Deeper trees capture complex patterns but cause overfitting.
clf = DecisionTreeClassifier(max_depth=5)

# Min Samples Split: Minimum samples required to split an internal node. 
# Higher values prevent the creation of highly specific branches.
clf = DecisionTreeClassifier(min_samples_split=10)

# Min Samples Leaf: Minimum samples required to exist inside a final leaf node. 
# Higher values smooth the model by smoothing out noise.
clf = DecisionTreeClassifier(min_samples_leaf=5)
```

### 2. Feature & Quality Parameters

```python
# Max Features: Limits the number of features considered when looking for the best split. 
# Restricting this introduces randomness to prevent overfitting.
clf = DecisionTreeClassifier(max_features='sqrt')

# Criterion: The mathematical function used to measure split quality.
# Options: 'gini' (Gini Impurity) or 'entropy' (Information Gain).
clf = DecisionTreeClassifier(criterion='entropy')
```

---

## 🔍 Optimization & Search Techniques

### 1. Grid Search
Systematically evaluates every single combination of parameters defined within a cross-product grid.

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth':,
    'min_samples_split':,
    'min_samples_leaf':,
    'criterion': ['gini', 'entropy'],
}

grid_search = GridSearchCV(
    DecisionTreeClassifier(), param_grid, cv=5, scoring='accuracy'
)
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
```

### 2. Random Search
Selects a fixed number of random parameter combinations from defined distributions to save computational time.

```python
import numpy as np
from sklearn.model_selection import RandomizedSearchCV

param_dist = {
    'max_depth': np.arange(3, 15),
    'min_samples_split': np.arange(2, 10),
    'min_samples_leaf': np.arange(1, 5),
}

random_search = RandomizedSearchCV(
    DecisionTreeClassifier(),
    param_distributions=param_dist,
    n_iter=10,
    cv=5,
    scoring='accuracy',
)
random_search.fit(X_train, y_train)

print("Best parameters:", random_search.best_params_)
```

### 3. Cross-Validation Score
Splits data into multiple operational folds to ensure the model generalizes consistently across different subsets.

```python
from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(DecisionTreeClassifier(), X, y, cv=5)
print("Cross-validation accuracy:", np.mean(cv_scores))
```

---

## 🏆 Production-Ready Optimized Model

This final step extracts the optimal hyperparameters identified during search optimization to construct a highly resilient Decision Tree.

```python
# Extract and unpack optimal configurations
best_params = grid_search.best_params_
optimized_clf = DecisionTreeClassifier(**best_params)

# Train the production model
optimized_clf.fit(X_train, y_train)

# Evaluate performance
y_pred_optimized = optimized_clf.predict(X_test)
accuracy_optimized = accuracy_score(y_test, y_pred_optimized)

print(f"Optimized Accuracy: {accuracy_optimized:.2f}")
```

---

## 📋 Summary

| Goal | Hyperparameter Adjustments |
| :--- | :--- |
| **Reduce Overfitting** | Decrease `max_depth` \| Increase `min_samples_split` \| Increase `min_samples_leaf` |
| **Reduce Underfitting** | Increase `max_depth` \| Decrease `min_samples_split` \| Decrease `min_samples_leaf` |
