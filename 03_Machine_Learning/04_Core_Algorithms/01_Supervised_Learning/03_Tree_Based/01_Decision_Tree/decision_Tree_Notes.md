# Decision Tree — Complete Machine Learning Notes

> **Category:** Supervised Learning → Tree-Based Models  
> **Tasks:** Classification + Regression  
> **Core idea:** Recursively split the dataset into smaller groups using feature-based decision rules.

---

## 1. What is a Decision Tree?

A **Decision Tree** is a supervised machine-learning algorithm that makes predictions by learning a sequence of decision rules from the training data.

It looks like a tree:

```text
                    Root
                     |
              Age < 30?
             /          \
           Yes           No
           /              \
     Income < 50K?       Yes
       /      \            |
     No       Yes        Class B
     |         |
 Class A     Class B
```

Each internal node asks a question about a feature.

Each branch represents the answer to that question.

Each leaf node represents the final prediction.

---

# 2. Why is it called a Tree?

The model has a hierarchical structure:

```text
Root
 |
 +---- Decision
 |      |
 |      +---- Decision
 |      |      |
 |      |      +---- Leaf
 |      |
 |      +---- Leaf
 |
 +---- Decision
        |
        +---- Leaf
```

Important terminology:

| Term | Meaning |
|---|---|
| Root node | First/top decision |
| Internal node | Decision/split inside the tree |
| Branch | Result of a decision |
| Leaf node | Final prediction |
| Parent node | Node that is split |
| Child node | Resulting node after a split |
| Depth | Distance from root |
| Subtree | Any smaller tree inside the complete tree |

---

# 3. Example

Suppose we want to predict whether a person will buy a laptop.

Features:

```text
Age
Income
Student
Credit Score
```

Target:

```text
Buy Laptop
```

A tree might learn:

```text
                  Student?
                 /        \
              Yes          No
              /             \
        Income > 50K?      Age > 30?
          /     \           /      \
        Yes     No        Yes      No
         |       |          |        |
        Buy    Don't      Buy      Don't
```

The model has learned a sequence of rules from the training data.

---

# 4. Decision Trees are Supervised Learning

Decision Trees require labelled training data.

For classification:

```text
X → Features
y → Class
```

Example:

```text
Age  Income  Student  → Buy
25   30000   Yes      → Yes
40   80000   No       → Yes
22   25000   No       → No
```

For regression:

```text
X → Features
y → Continuous value
```

Example:

```text
Area  Bedrooms → Price
1000     2     → 40
1500     3     → 65
2000     4     → 90
```

---

# 5. Classification vs Regression Trees

Decision Trees can solve both major supervised-learning tasks.

## Classification Tree

Output is a class.

Examples:

```text
Spam / Not Spam
Disease / No Disease
Cat / Dog
Pass / Fail
```

Common splitting criteria:

- Gini Impurity
- Entropy
- Information Gain

---

## Regression Tree

Output is a numerical value.

Examples:

```text
House price
Temperature
Salary
Demand
```

Common splitting objective:

- Mean Squared Error
- Variance reduction

---

# 6. How Does a Decision Tree Learn?

The basic process is:

```text
Training Data
      ↓
Find the best split
      ↓
Split the data
      ↓
Find the best split in each subset
      ↓
Repeat recursively
      ↓
Stop according to stopping criteria
      ↓
Final Decision Tree
```

The central question is:

> **Which feature and threshold should I use for the next split?**

---

# 7. What is a Split?

A split divides the dataset into smaller subsets.

For example:

```text
Age < 30
```

creates:

```text
Left child:
Age < 30

Right child:
Age >= 30
```

For a categorical feature:

```text
Weather = Sunny
```

could divide observations according to category.

---

# 8. Binary Splits

Many implementations use binary splits.

Example:

```text
Income <= 50000?
       /       \
     Yes       No
```

This produces two child nodes.

For numerical features, the tree searches for a threshold.

Example:

```text
Age <= 25
Age <= 30
Age <= 35
Age <= 40
```

The algorithm evaluates possible thresholds and chooses the one that gives the best improvement according to its splitting criterion.

---

# 9. Impurity

A decision tree wants its child nodes to be as **pure** as possible.

A pure node contains mostly one class.

Example:

```text
Node A:
Dog
Dog
Dog
Dog
```

This is completely pure.

Another node:

```text
Node B:
Dog
Cat
Dog
Cat
```

This is impure.

The goal is approximately:

```text
High impurity
      ↓
Split
      ↓
Lower impurity
```

---

# 10. Gini Impurity

Gini impurity is commonly used for classification trees.

Formula:

\[
Gini = 1-\sum_{i=1}^{K}p_i^2
\]

where:

- \(K\) = number of classes
- \(p_i\) = proportion of samples belonging to class \(i\)

---

## Binary Example

Suppose a node contains:

```text
10 samples

6 → Yes
4 → No
```

Therefore:

\[
p(Yes)=0.6
\]

\[
p(No)=0.4
\]

Then:

\[
Gini = 1-(0.6^2+0.4^2)
\]

\[
=1-(0.36+0.16)
\]

\[
=0.48
\]

So:

```text
Gini = 0.48
```

---

# 11. Gini Interpretation

For binary classification:

### Perfectly pure node

```text
10 Yes
0 No
```

\[
Gini=1-(1^2+0^2)=0
\]

So:

```text
Gini = 0
```

Perfect purity.

---

### Maximum impurity

For two classes:

```text
5 Yes
5 No
```

\[
Gini=1-(0.5^2+0.5^2)
\]

\[
Gini=0.5
\]

Therefore for binary classification:

```text
Gini = 0      → Pure
Gini = 0.5    → Maximum impurity
```

For \(K\) classes, the maximum is:

\[
1-\frac{1}{K}
\]

---

# 12. Entropy

Entropy measures uncertainty or impurity.

Formula:

\[
H(S)=-\sum_{i=1}^{K}p_i\log_2(p_i)
\]

For binary classification:

\[
H(S)
=
-p_{Yes}\log_2(p_{Yes})
-
p_{No}\log_2(p_{No})
\]

---

## Example

Suppose:

```text
6 Yes
4 No
```

Then:

\[
p_{Yes}=0.6
\]

\[
p_{No}=0.4
\]

Therefore:

\[
H(S)
=
-(0.6\log_2 0.6)
-
(0.4\log_2 0.4)
\]

Approximately:

\[
H(S)\approx0.971
\]

---

# 13. Entropy Interpretation

For binary classification:

```text
Entropy = 0
```

means perfectly pure.

```text
Entropy = 1
```

means maximum uncertainty.

Therefore:

```text
Lower entropy → Better purity
Higher entropy → More uncertainty
```

---

# 14. Information Gain

Information Gain measures how much a split reduces uncertainty.

Formula:

\[
IG(S,A)
=
H(S)
-
\sum_{v\in Values(A)}
\frac{|S_v|}{|S|}
H(S_v)
\]

In simple terms:

```text
Information Gain
=
Parent Entropy
-
Weighted Child Entropy
```

The algorithm prefers a split with **higher Information Gain**.

---

# 15. Information Gain Example

Suppose:

```text
Parent:

10 samples
6 Yes
4 No
```

Parent entropy:

\[
H(parent)\approx0.971
\]

Suppose a split creates:

```text
Child 1:
5 samples
5 Yes
0 No

Child 2:
5 samples
1 Yes
4 No
```

Child 1:

\[
H(child_1)=0
\]

Child 2:

\[
H(child_2)
\approx0.722
\]

Weighted child entropy:

\[
\frac{5}{10}(0)+
\frac{5}{10}(0.722)
\]

\[
=0.361
\]

Therefore:

\[
IG=0.971-0.361
\]

\[
IG\approx0.610
\]

Higher Information Gain means a better split.

---

# 16. Gini vs Information Gain

| Property | Gini | Entropy / Information Gain |
|---|---|---|
| Used for | Classification | Classification |
| Measures | Impurity | Uncertainty |
| Best split | Lower weighted Gini | Higher Information Gain |
| Calculation | Relatively simpler | Uses logarithms |
| Common in | CART / sklearn | ID3-style trees |

Important:

```text
Gini:
Lower is better

Information Gain:
Higher is better
```

---

# 17. Gain Ratio

Information Gain can sometimes favour attributes with many distinct values.

**Gain Ratio** attempts to compensate for this.

\[
GainRatio=
\frac{Information\ Gain}{Split\ Information}
\]

Split Information:

\[
SplitInfo=
-\sum_v
\frac{|S_v|}{|S|}
\log_2
\left(
\frac{|S_v|}{|S|}
\right)
\]

Gain Ratio is associated particularly with **C4.5**.

---

# 18. CART

**CART** stands for:

> Classification and Regression Trees

CART constructs binary decision trees.

It can be used for:

```text
Classification
Regression
```

Commonly associated splitting criteria:

```text
Classification → Gini impurity
Regression     → Squared-error / variance-related criteria
```

Scikit-learn's `DecisionTreeClassifier` and `DecisionTreeRegressor` are based on an optimized CART-style approach.

---

# 19. ID3

**ID3** stands for:

> Iterative Dichotomiser 3

Main characteristics:

- Classification
- Uses Entropy
- Uses Information Gain
- Historically important
- Originally designed mainly for categorical attributes

Basic process:

```text
Calculate entropy
       ↓
Calculate information gain
       ↓
Choose highest-gain feature
       ↓
Split
       ↓
Repeat
```

---

# 20. C4.5

C4.5 is an extension of ID3.

Important features:

- Uses Gain Ratio
- Handles continuous attributes
- Handles missing values
- Supports pruning
- More robust than basic ID3

---

# 21. CART vs ID3 vs C4.5

| Algorithm | Main Criterion | Binary Tree | Regression |
|---|---|---:|---:|
| ID3 | Information Gain | Not necessarily | No |
| C4.5 | Gain Ratio | Not necessarily | No |
| CART | Gini / squared-error style | Yes | Yes |

For modern practical ML with scikit-learn, **CART-style trees are the important implementation to understand**.

---

# 22. Decision Tree Training Algorithm

General algorithm:

```text
1. Start with the complete training dataset.

2. Check possible features.

3. For each feature:
   Evaluate possible splits.

4. Calculate the split quality.

5. Select the best split.

6. Divide the dataset.

7. Repeat the process recursively
   for each child node.

8. Stop when a stopping condition is reached.

9. Assign predictions to leaf nodes.
```

---

# 23. Recursive Partitioning

Decision Trees use **recursive partitioning**.

Example:

```text
Dataset
   |
   +--- Age < 30
   |       |
   |       +--- Income < 40K
   |
   +--- Age >= 30
           |
           +--- Credit Score > 700
```

Each split creates a smaller subproblem.

The process continues until the stopping condition is reached.

---

# 24. Stopping Criteria

A tree does not have to keep splitting forever.

Common stopping conditions:

- Maximum depth reached
- Minimum number of samples required to split
- Minimum number of samples in a leaf
- No useful improvement
- Node becomes pure
- Maximum number of leaf nodes reached

Important hyperparameters in scikit-learn include:

```text
max_depth
min_samples_split
min_samples_leaf
max_leaf_nodes
min_impurity_decrease
```

---

# 25. Why Trees Overfit

A Decision Tree can become extremely complicated:

```text
Training Data
     ↓
Many splits
     ↓
Very deep tree
     ↓
Almost memorizes training data
     ↓
Training accuracy ≈ 100%
     ↓
Poor generalization
```

This is **overfitting**.

---

# 26. Underfitting

If the tree is too simple:

```text
Very shallow tree
      ↓
Cannot capture useful patterns
      ↓
Poor training performance
      ↓
Poor test performance
```

This is **underfitting**.

---

# 27. Bias-Variance Relationship

Generally:

```text
Very shallow tree
→ High bias
→ Low variance
→ Underfitting

Very deep tree
→ Low bias
→ High variance
→ Overfitting
```

Therefore, tree complexity must be controlled.

This connects directly to the bias-variance tradeoff in your ML roadmap.

---

# 28. Pre-Pruning

**Pre-pruning** prevents the tree from becoming unnecessarily large during training.

Examples:

```python
DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5
)
```

Important parameters:

### `max_depth`

Controls maximum tree depth.

Smaller:

```text
Less complexity
Less overfitting
```

Larger:

```text
More complexity
Higher overfitting risk
```

---

### `min_samples_split`

Minimum number of samples required to split an internal node.

Example:

```text
min_samples_split = 10
```

A node containing fewer than 10 samples cannot be split.

---

### `min_samples_leaf`

Minimum number of samples required in a leaf.

Example:

```text
min_samples_leaf = 5
```

Prevents extremely small leaves.

---

# 29. Post-Pruning

Another approach is:

```text
Grow tree
   ↓
Remove unnecessary branches
   ↓
Simpler tree
```

This is called **post-pruning**.

The purpose is to improve generalization and reduce unnecessary complexity.

---

# 30. Cost-Complexity Pruning

CART-style trees can use **cost-complexity pruning**.

The objective can be represented as:

\[
R_\alpha(T)
=
R(T)+\alpha|T|
\]

where:

- \(R(T)\) = tree error
- \(|T|\) = number of leaves
- \(\alpha\) = complexity penalty

Interpretation:

```text
Model error
+
Complexity penalty
```

Larger \(\alpha\):

```text
More aggressive pruning
→ Smaller tree
```

In scikit-learn this is controlled using:

```python
ccp_alpha
```

---

# 31. Decision Tree Regression

For regression, the target is continuous.

Example:

```text
House:
Area → Price
```

Suppose a leaf contains:

```text
40
45
50
55
```

A regression tree commonly predicts the mean:

\[
\hat{y}
=
\frac{40+45+50+55}{4}
\]

\[
\hat{y}=47.5
\]

So each leaf produces a numerical prediction.

---

# 32. Regression Splitting

The tree searches for splits that reduce prediction error.

One common criterion is squared error.

For a node:

\[
MSE =
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\bar y)^2
\]

where:

\[
\bar y
=
\frac{1}{n}
\sum y_i
\]

The algorithm prefers splits that reduce the weighted error.

---

# 33. Classification Prediction

Suppose a leaf contains:

```text
Yes = 8
No = 2
```

The predicted class is usually:

```text
Yes
```

because it is the majority class.

The class probability can be estimated as:

\[
P(Yes)=\frac{8}{10}=0.8
\]

\[
P(No)=\frac{2}{10}=0.2
\]

Therefore:

```text
Predicted class = Yes
Probability = 0.80
```

---

# 34. Important Characteristics

Decision Trees are:

### Non-parametric

They do not assume that the data follows a particular distribution.

### Non-linear

They can model nonlinear relationships.

### Rule-based

They learn decision rules.

### Hierarchical

Decisions are made sequentially.

---

# 35. Feature Scaling

Decision Trees generally **do not require feature scaling**.

For example:

```text
Age:        18–80
Salary:     20,000–2,00,000
```

A tree can still split on these features without standardization.

Therefore, unlike algorithms such as:

- KNN
- SVM
- Logistic Regression

you generally do not need StandardScaler merely because you are using a Decision Tree.

---

# 36. Numerical Features

Trees can naturally handle numerical features.

Example:

```text
Age <= 35
```

Possible thresholds:

```text
Age <= 20
Age <= 25
Age <= 30
Age <= 35
Age <= 40
```

The algorithm searches for a useful threshold.

---

# 37. Categorical Features

Conceptually, Decision Trees can split categorical variables.

However, **scikit-learn's traditional `DecisionTreeClassifier` expects numerical input**, so categorical features generally need preprocessing such as one-hot encoding.

Example:

```text
Color:
Red
Blue
Green
```

One-hot encoding:

```text
Red   Blue   Green
1      0      0
0      1      0
0      0      1
```

This connects to the preprocessing topics in your roadmap.

---

# 38. Missing Values

Missing-value handling depends on the specific implementation.

A safe practical workflow is:

```text
Raw Data
   ↓
Detect missing values
   ↓
Impute / otherwise handle them
   ↓
Train Decision Tree
```

Do not assume every Decision Tree implementation automatically handles missing values in the same way.

---

# 39. Advantages

### 1. Easy to understand

The model can be represented as human-readable rules.

### 2. Nonlinear relationships

Trees can capture nonlinear decision boundaries.

### 3. Little preprocessing

Feature scaling is generally unnecessary.

### 4. Handles classification and regression

One algorithm family supports both.

### 5. Feature selection is built into splitting

The tree naturally chooses useful features for its splits.

### 6. Interpretable

A trained tree can be visualized.

---

# 40. Disadvantages

### 1. Overfitting

Unrestricted trees can memorize training data.

### 2. High variance

Small changes in the training dataset can sometimes produce a substantially different tree.

### 3. Greedy learning

The standard tree-building process makes locally optimal split decisions rather than solving a globally optimal tree search.

### 4. Large trees become difficult to interpret

A tree with hundreds of nodes is no longer practically understandable.

### 5. Usually weaker than ensembles

A single tree is often less accurate and less robust than methods such as:

```text
Random Forest
Gradient Boosting
XGBoost
LightGBM
CatBoost
```

Your roadmap specifically places these algorithms after Decision Trees under Tree-Based Models.

---

# 41. Decision Boundary

A Decision Tree creates **piecewise decision regions**.

For two numerical features:

```text
Feature 2
   ^
   |
   |     Class A
   |     |
   |-----|---------
   |     |
   | Class B
   |
   +-----------------> Feature 1
```

Splits are typically axis-aligned:

```text
x <= threshold
```

or

```text
y <= threshold
```

Therefore the resulting classification regions can look rectangular.

---

# 42. Why Decision Trees Can Model Nonlinear Data

Consider:

\[
y =
\begin{cases}
1 & x_1 > 5 \text{ and } x_2 < 3\\
0 & otherwise
\end{cases}
\]

A tree can approximate this using multiple rules:

```text
x1 > 5?
   |
   +--- No → Class 0
   |
   +--- Yes
         |
       x2 < 3?
        /    \
      Yes     No
       |       |
    Class 1  Class 0
```

No linear equation is required.

---

# 43. Feature Importance

Decision Trees can provide feature-importance scores.

A feature receives importance based on its contribution to impurity reduction across the tree.

Example:

```text
Feature        Importance
Income         0.45
Age            0.30
Credit Score   0.20
Student        0.05
```

Important:

> Feature importance from a tree should not automatically be interpreted as causal importance.

Also, impurity-based importance can be biased toward certain feature types, especially high-cardinality features.

---

# 44. Decision Tree vs Linear Regression

| Property | Decision Tree | Linear Regression |
|---|---|---|
| Relationship | Nonlinear | Linear |
| Output | Class/value | Continuous value |
| Scaling | Usually unnecessary | Often useful depending on workflow |
| Interpretability | High | High |
| Splits | Yes | No |
| Regression | Yes | Yes |

---

# 45. Decision Tree vs Logistic Regression

| Property | Decision Tree | Logistic Regression |
|---|---|---|
| Task | Classification + regression | Classification |
| Boundary | Nonlinear | Linear unless features are transformed |
| Scaling | Usually unnecessary | Often useful |
| Interpretability | Rule-based | Coefficient-based |
| Overfitting | High risk for deep trees | Controlled with regularization |

---

# 46. Decision Tree vs KNN

| Property | Decision Tree | KNN |
|---|---|---|
| Learning style | Tree-based | Instance-based |
| Scaling | Usually unnecessary | Important |
| Prediction | Follow rules | Find neighbours |
| Training | Builds tree | Minimal training |
| Prediction cost | Usually low | Can be relatively expensive |

---

# 47. Decision Tree vs Random Forest

A Random Forest combines many Decision Trees.

```text
Decision Tree
      ↓
One tree

Random Forest
      ↓
Tree 1
Tree 2
Tree 3
...
Tree N
      ↓
Combine predictions
```

Single tree:

```text
Higher interpretability
Higher variance
```

Random Forest:

```text
Lower variance
Usually better generalization
Less interpretable
```

---

# 48. Decision Tree vs Gradient Boosting

Decision Trees can also act as **base learners** in boosting algorithms.

```text
Tree 1
  ↓
Find errors
  ↓
Tree 2
  ↓
Correct errors
  ↓
Tree 3
  ↓
...
```

This leads to algorithms such as:

- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

These are specifically identified as important tree-based models in your roadmap.

---

# 49. Scikit-learn Classification

Basic implementation:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

---

# 50. Entropy Criterion

```python
model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5,
    random_state=42
)
```

Some scikit-learn versions also support:

```python
criterion="log_loss"
```

for classification.

---

# 51. Regression

```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

---

# 52. Important Hyperparameters

For `DecisionTreeClassifier`:

```python
DecisionTreeClassifier(
    criterion="gini",
    splitter="best",
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features=None,
    max_leaf_nodes=None,
    min_impurity_decrease=0.0,
    class_weight=None,
    ccp_alpha=0.0,
    random_state=None
)
```

The most important ones to understand first are:

```text
criterion
max_depth
min_samples_split
min_samples_leaf
max_leaf_nodes
class_weight
ccp_alpha
```

Do not try to memorize every parameter initially.

---

# 53. `criterion`

Classification:

```python
criterion="gini"
```

or:

```python
criterion="entropy"
```

Regression:

```python
criterion="squared_error"
```

Other regression criteria are also available depending on the implementation/version.

---

# 54. `max_depth`

Example:

```python
DecisionTreeClassifier(max_depth=3)
```

Controls maximum depth.

Conceptually:

```text
max_depth = 2

        Root
       /    \
      /      \
    Node    Node
```

Smaller depth:

```text
Simpler model
```

Larger depth:

```text
More complex model
```

---

# 55. `min_samples_split`

```python
DecisionTreeClassifier(
    min_samples_split=10
)
```

A node must have at least 10 samples before it can be split.

This helps control tree complexity.

---

# 56. `min_samples_leaf`

```python
DecisionTreeClassifier(
    min_samples_leaf=5
)
```

Every leaf must contain at least 5 samples.

This can prevent extremely specific rules.

---

# 57. `class_weight`

Useful for imbalanced classification.

Example:

```python
DecisionTreeClassifier(
    class_weight="balanced"
)
```

This gives more importance to minority classes according to the class frequencies.

Your roadmap explicitly includes handling imbalanced data through techniques such as class weights and SMOTE.

---

# 58. `ccp_alpha`

Controls cost-complexity pruning.

```python
DecisionTreeClassifier(
    ccp_alpha=0.01
)
```

Larger value:

```text
More pruning
→ Smaller tree
```

---

# 59. Visualizing a Decision Tree

Scikit-learn provides:

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=True,
    filled=True
)

plt.show()
```

This is particularly useful for understanding how the model makes decisions.

---

# 60. Evaluating Classification

Use a suitable classification metric.

### Accuracy

\[
Accuracy =
\frac{Correct\ Predictions}{Total\ Predictions}
\]

Python:

```python
from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)
```

---

### Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, y_pred)
```

Structure:

```text
                 Predicted
               Positive Negative
Actual Positive    TP       FN
       Negative    FP       TN
```

---

### Precision

\[
Precision =
\frac{TP}{TP+FP}
\]

---

### Recall

\[
Recall =
\frac{TP}{TP+FN}
\]

---

### F1 Score

\[
F1 =
2\frac{Precision \times Recall}
{Precision+Recall}
\]

These evaluation metrics are explicitly part of the ML-engineering section of your roadmap.

---

# 61. Evaluating Regression Trees

Common metrics:

### MAE

\[
MAE=
\frac{1}{n}
\sum |y_i-\hat y_i|
\]

### MSE

\[
MSE=
\frac{1}{n}
\sum(y_i-\hat y_i)^2
\]

### RMSE

\[
RMSE=\sqrt{MSE}
\]

### \(R^2\)

\[
R^2=
1-
\frac{SS_{res}}
{SS_{tot}}
\]

---

# 62. Train/Test Split

A typical workflow:

```text
Dataset
   |
   +------ Training data
   |
   +------ Testing data
```

Example:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

For classification, `stratify=y` is often useful when preserving class proportions matters.

---

# 63. Cross-Validation

Instead of relying on a single train/test split, use cross-validation.

Example:

```text
Fold 1 → Train / Validation
Fold 2 → Train / Validation
Fold 3 → Train / Validation
Fold 4 → Train / Validation
Fold 5 → Train / Validation
```

Then average the validation scores.

This is useful for choosing:

```text
max_depth
min_samples_split
min_samples_leaf
ccp_alpha
```

Cross-validation is explicitly part of the core ML theory in your roadmap.

---

# 64. Hyperparameter Tuning

Example:

```python
from sklearn.model_selection import GridSearchCV

params = {
    "max_depth": [3, 5, 7, 10],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 5]
}

grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    params,
    cv=5,
    scoring="accuracy"
)

grid.fit(X_train, y_train)

print(grid.best_params_)
```

---

# 65. Complete Practical Workflow

```text
1. Load dataset
       ↓
2. Understand features and target
       ↓
3. Clean data
       ↓
4. Handle missing values
       ↓
5. Encode categorical variables if necessary
       ↓
6. Split train/test
       ↓
7. Train Decision Tree
       ↓
8. Evaluate baseline
       ↓
9. Check overfitting
       ↓
10. Tune hyperparameters
       ↓
11. Cross-validation
       ↓
12. Evaluate final model
       ↓
13. Visualize tree
       ↓
14. Analyze feature importance
       ↓
15. Save/deploy model if required
```

---

# 66. A Simple Mental Model

Think of a Decision Tree as a sequence of questions.

Example:

```text
Is age <= 30?
      |
   Yes/No
      ↓
Is income <= 50K?
      |
   Yes/No
      ↓
Is student = Yes?
      |
   Yes/No
      ↓
Prediction
```

The machine-learning algorithm's job is to discover:

```text
Which question?
        ↓
Which feature?
        ↓
Which threshold?
        ↓
In what order?
        ↓
When should we stop?
```

---

# 67. Most Important Mathematical Concepts

For a strong ML-engineer understanding, know these:

### Classification

```text
Gini Impurity
Entropy
Information Gain
Gain Ratio
```

### Regression

```text
Mean
Variance
MSE
Variance reduction
```

### Model complexity

```text
Depth
Number of leaves
Pruning
Cost-complexity
```

---

# 68. Interview Questions

You should be able to answer these without notes:

### Basic

1. What is a Decision Tree?
2. Is Decision Tree supervised or unsupervised?
3. Can Decision Trees perform regression?
4. What are root, internal, branch, and leaf nodes?
5. How does a Decision Tree make predictions?

### Splitting

6. What is a split?
7. What is impurity?
8. What is Gini impurity?
9. What is entropy?
10. What is Information Gain?
11. Difference between Gini and Entropy?
12. What is Gain Ratio?
13. Why does a Decision Tree choose a particular feature?

### Overfitting

14. Why do Decision Trees overfit?
15. How do you prevent Decision Tree overfitting?
16. What is `max_depth`?
17. What is `min_samples_split`?
18. What is `min_samples_leaf`?
19. What is pruning?
20. What is cost-complexity pruning?

### Practical

21. Does a Decision Tree require feature scaling?
22. How do you handle categorical variables?
23. How do you handle missing values?
24. How do you evaluate a classification tree?
25. How do you evaluate a regression tree?
26. How do you visualize a Decision Tree?
27. What is feature importance?
28. What happens if the tree is too deep?

### Advanced

29. What is CART?
30. What is ID3?
31. What is C4.5?
32. Why are Decision Trees considered high variance?
33. Why are trees called non-parametric?
34. Why can trees model nonlinear relationships?
35. Why does Random Forest generally outperform a single Decision Tree?

---

# 69. Common Mistakes

### Mistake 1

> "Highest Gini is the best split."

Incorrect.

```text
Lower Gini → Better
```

---

### Mistake 2

> "Lowest Information Gain is best."

Incorrect.

```text
Higher Information Gain → Better
```

---

### Mistake 3

> "Decision Trees always require StandardScaler."

Incorrect.

Trees generally do not require feature scaling.

---

### Mistake 4

> "A deeper tree is always better."

Incorrect.

A very deep tree can overfit.

---

### Mistake 5

> "Decision Trees are always interpretable."

Only small/simple trees are practically interpretable.

---

### Mistake 6

> "Feature importance means causation."

Incorrect.

Feature importance describes contribution to the model's decision process, not causal influence.

---

# 70. What You Actually Need to Master

For your AI/ML Engineer roadmap, prioritize:

## Level 1 — Must Know

```text
✓ What is Decision Tree?
✓ Classification vs Regression
✓ Root / Node / Branch / Leaf
✓ Splitting
✓ Gini Impurity
✓ Entropy
✓ Information Gain
✓ Overfitting
✓ max_depth
✓ min_samples_split
✓ min_samples_leaf
✓ Prediction process
✓ Evaluation metrics
```

## Level 2 — Strong Understanding

```text
✓ CART
✓ ID3
✓ C4.5
✓ Gain Ratio
✓ Regression Trees
✓ Pruning
✓ Cost-complexity pruning
✓ Feature importance
✓ Cross-validation
✓ Hyperparameter tuning
```

## Level 3 — Interview/Advanced

```text
✓ Why trees have high variance
✓ Greedy splitting
✓ Bias-variance tradeoff
✓ Computational considerations
✓ Handling class imbalance
✓ Decision boundaries
✓ Relationship with Random Forest
✓ Relationship with Gradient Boosting
```

---

# 71. Decision Tree Cheat Sheet

```text
Decision Tree
│
├── Supervised Learning
│
├── Tasks
│   ├── Classification
│   └── Regression
│
├── Structure
│   ├── Root
│   ├── Internal Nodes
│   ├── Branches
│   └── Leaves
│
├── Classification Splitting
│   ├── Gini Impurity
│   ├── Entropy
│   ├── Information Gain
│   └── Gain Ratio
│
├── Regression Splitting
│   ├── MSE
│   └── Variance Reduction
│
├── Algorithms
│   ├── ID3
│   ├── C4.5
│   └── CART
│
├── Complexity Control
│   ├── max_depth
│   ├── min_samples_split
│   ├── min_samples_leaf
│   ├── max_leaf_nodes
│   └── ccp_alpha
│
├── Problems
│   ├── Overfitting
│   └── High Variance
│
├── Advantages
│   ├── Interpretable
│   ├── Nonlinear
│   ├── Little preprocessing
│   └── Classification + Regression
│
└── Ensembles
    ├── Random Forest
    ├── Gradient Boosting
    ├── XGBoost
    ├── LightGBM
    └── CatBoost
```

---

# 72. Final Learning Checklist

- [ ] Understand what a Decision Tree is
- [ ] Understand tree terminology
- [ ] Understand classification trees
- [ ] Understand regression trees
- [ ] Understand how splitting works
- [ ] Learn Gini impurity
- [ ] Learn entropy
- [ ] Learn Information Gain
- [ ] Learn Gain Ratio
- [ ] Understand CART
- [ ] Understand ID3
- [ ] Understand C4.5
- [ ] Understand recursive partitioning
- [ ] Understand stopping criteria
- [ ] Understand overfitting
- [ ] Understand bias-variance tradeoff
- [ ] Learn pre-pruning
- [ ] Learn post-pruning
- [ ] Understand `max_depth`
- [ ] Understand `min_samples_split`
- [ ] Understand `min_samples_leaf`
- [ ] Understand `ccp_alpha`
- [ ] Understand regression-tree MSE
- [ ] Understand feature importance
- [ ] Understand decision boundaries
- [ ] Understand why scaling is usually unnecessary
- [ ] Practice `DecisionTreeClassifier`
- [ ] Practice `DecisionTreeRegressor`
- [ ] Visualize a tree with `plot_tree`
- [ ] Evaluate classification performance
- [ ] Evaluate regression performance
- [ ] Practice cross-validation
- [ ] Practice hyperparameter tuning
- [ ] Understand Decision Tree vs Random Forest
- [ ] Understand Decision Tree vs Gradient Boosting
- [ ] Solve Decision Tree interview questions

---

## Mastery Standard

You can consider **Decision Tree complete** for your current ML roadmap when you can do all four of these:

```text
THEORY
   ↓
Explain how the tree chooses a split
   ↓
MATH
   ↓
Calculate Gini, Entropy and Information Gain manually
   ↓
IMPLEMENTATION
   ↓
Train + tune + visualize a DecisionTreeClassifier/Regressor
   ↓
INTERVIEW
   ↓
Explain overfitting, pruning, CART and
Decision Tree vs Random Forest
```

The next natural topic in your roadmap is **Random Forest**, followed by **Gradient Boosting → XGBoost/LightGBM/CatBoost**.