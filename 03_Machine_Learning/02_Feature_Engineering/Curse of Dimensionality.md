# Curse of Dimensionality

## 1. Definition
The **Curse of Dimensionality** refers to various problems that arise when working with data in **high-dimensional spaces** (i.e., when the number of features increases significantly).

As dimensions increase, data becomes sparse and many machine learning algorithms perform poorly.

---

## 2. Key Problems

### 2.1 Data Sparsity
- In high dimensions, data points are far apart from each other.
- Hard to find meaningful patterns or clusters.

---

### 2.2 Distance Becomes Meaningless
- Algorithms like kNN rely on distance.
- In high dimensions:
  - Distance between nearest and farthest points becomes almost equal.
  - This makes similarity measures unreliable.

---

### 2.3 Overfitting
- More features → more complexity
- Model starts memorizing instead of learning patterns

---

### 2.4 Increased Computation Cost
- More features → more calculations
- Training becomes slower and inefficient

---

## 3. Mathematical Intuition

As dimensions increase:
- Volume of space increases exponentially
- Data required to maintain density also increases exponentially

---

## 4. Impact on Algorithms

| Algorithm | Effect |
|----------|--------|
| kNN | Performs poorly due to unreliable distances |
| Clustering | Hard to form meaningful clusters |
| Linear Models | May overfit with too many features |
| Tree Models | Can handle better but still affected |

---

