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
