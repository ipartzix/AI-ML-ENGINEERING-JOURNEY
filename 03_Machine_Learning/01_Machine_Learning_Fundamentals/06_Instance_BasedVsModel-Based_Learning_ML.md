# Instance-Based vs Model-Based Learning
## (Types of Machine Learning Approaches)

Machine learning systems can also be categorized based on **how they learn from data**.  
Two important learning approaches are:

1. Instance-Based Learning
2. Model-Based Learning

These approaches describe **how the algorithm generalizes knowledge from data**.

---

# 1. Instance-Based Learning

## Definition

**Instance-Based Learning** is a machine learning approach where the model **memorizes the training data** and makes predictions by comparing new data points with the stored examples.

Instead of building an explicit model, the algorithm **uses similarity between instances** to make predictions.

Because it stores training examples, this method is also called:

- Memory-Based Learning
- Lazy Learning

---

## How Instance-Based Learning Works

1. Store the training dataset.
2. When a new data point arrives:
3. Compare it with stored data points.
4. Find the most similar instances.
5. Use those instances to make a prediction.

```

Training Data Stored → New Input → Similarity Comparison → Prediction

```

---

## Example

### K-Nearest Neighbors (KNN)

In **KNN**, the algorithm:

1. Stores all training data.
2. When a new input arrives, it calculates the **distance** between the new point and existing data.
3. It selects the **K nearest neighbors**.
4. The prediction is based on the **majority class or average value**.

Example:

If most neighbors belong to **Class A**, the new data point is classified as **Class A**.

---
## Characteristics of Instance-Based Learning

| Feature | Description |
|------|------|
| Learning Type | Lazy learning |
| Training Time | Very low |
| Prediction Time | High |
| Memory Usage | High |
| Model Structure | No explicit model |

---

## Advantages

### 1. Simple Implementation
Instance-based algorithms are easy to implement.

### 2. Flexible Learning
They can adapt easily to **complex decision boundaries**.

### 3. No Training Phase Required
Most of the computation happens during prediction.

---

## Disadvantages

### 1. High Memory Usage
The entire dataset must be stored.

### 2. Slow Prediction
Every prediction requires comparing with many stored instances.

### 3. Sensitive to Noise
Outliers can affect prediction accuracy.

---

## Common Instance-Based Algorithms

- K-Nearest Neighbors (KNN)
- Case-Based Reasoning
- Locally Weighted Learning

---

# 2. Model-Based Learning

## Definition

**Model-Based Learning** is a machine learning approach where the algorithm **builds a mathematical model from training data** and uses that model to make predictions.

Instead of storing all examples, the algorithm **learns patterns and relationships in the data**.

---

## How Model-Based Learning Works

1. Choose a model type.
2. Train the model on training data.
3. Learn parameters that fit the data.
4. Use the trained model for predictions.

```

Training Data → Model Training → Learn Parameters → Predict New Data

```

---

## Example

### Linear Regression

In **Linear Regression**, the model learns a mathematical relationship:

```

y = w₁x₁ + w₂x₂ + b

```

Where:

- `x` = input features
- `w` = learned weights
- `b` = bias

After training, the model uses this equation to predict values for new inputs.

---