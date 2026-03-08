# Types of Machine Learning

Machine Learning algorithms are generally categorized based on how they learn from data.  
The four primary types of Machine Learning are:

1. Supervised Learning
2. Unsupervised Learning
3. Semi-Supervised Learning
4. Reinforcement Learning


---

# 1. Supervised Learning

## Definition
Supervised Learning is a type of machine learning where the model is trained using **labeled data**.  
Each input data point has a corresponding **correct output (label)**.

The algorithm learns the relationship between **input features (X)** and **output labels (y)**.

```
Input (X) → Model → Output Prediction (y)
```

## Example

| Input | Output |
|------|------|
| Email Text | Spam / Not Spam |
| House Features | House Price |
| Patient Data | Disease / No Disease |

## Sub-Branches of Supervised Learning

### 1. Classification

Classification predicts **discrete categorical labels**.

Examples:
- Spam detection
- Image classification
- Sentiment analysis
- Disease detection

Example outputs:

```
Yes / No
Spam / Not Spam
Cat / Dog
Positive / Negative
```

Common Algorithms:

- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Neural Networks


---

### 2. Regression

Regression predicts **continuous numerical values**.

Examples:
- House price prediction
- Temperature forecasting
- Stock price estimation
- Sales prediction

Example outputs:

```
Price = 450000
Temperature = 32.4°C
```

Common Algorithms:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Polynomial Regression
- Decision Tree Regressor
- Random Forest Regressor


---

# 2. Unsupervised Learning

## Definition

Unsupervised Learning works with **unlabeled data**.  
The algorithm tries to **discover hidden patterns, structures, or relationships** in the data.

```
Input Data → Pattern Discovery
```

Example dataset:

Customer purchasing behavior without labels.

## Sub-Branches of Unsupervised Learning

### 1. Clustering

Clustering groups **similar data points together**.

Example:

Customer segmentation:

```
Group 1 → Budget customers
Group 2 → Premium customers
Group 3 → Occasional buyers
```

Common Algorithms:

- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Gaussian Mixture Models


---

### 2. Dimensionality Reduction

Reduces the **number of features while preserving important information**.

Purpose:

- Simplify datasets
- Reduce computation cost
- Improve visualization
- Remove noise

Example:

```
100 features → Reduced to 10 important features
```

Common Algorithms:

- Principal Component Analysis (PCA)
- t-SNE
- UMAP
- Autoencoders


---

### 3. Association Rule Learning

Finds **relationships between variables in large datasets**.

Example:

Market Basket Analysis:

```
If customer buys Bread → likely buys Butter
```

Applications:

- Recommendation systems
- Retail analytics

Common Algorithms:

- Apriori Algorithm
- FP-Growth


---

# 3. Semi-Supervised Learning

## Definition

Semi-Supervised Learning uses a **small amount of labeled data** combined with **a large amount of unlabeled data**.

This approach is useful when labeling data is **expensive or time-consuming**.

Example:

Medical imaging datasets where only a small portion of images are labeled.

```
Small labeled dataset
+
Large unlabeled dataset
→ Improved model performance
```

Applications:

- Image recognition
- Speech recognition
- Text classification


---

# 4. Reinforcement Learning

## Definition

Reinforcement Learning is a type of learning where an **agent interacts with an environment** and learns by receiving **rewards or penalties**.

The goal is to learn a **policy that maximizes cumulative reward**.

## Key Components

Agent  
The learning system.

Environment  
The world the agent interacts with.

Action  
Choices made by the agent.

Reward  
Feedback from the environment.

Policy  
Strategy used by the agent.

## Learning Process

```
Agent → Action → Environment
       ↑          ↓
     Reward ← Feedback
```

## Applications

- Self-driving cars
- Game playing (Chess, Go)
- Robotics
- Recommendation systems

Algorithms:

- Q-Learning
- Deep Q Networks (DQN)
- Policy Gradient Methods
- Actor-Critic Methods


---

# Summary

| Type | Data Type | Goal |
|-----|-----|-----|
| Supervised Learning | Labeled Data | Predict outputs |
| Unsupervised Learning | Unlabeled Data | Discover patterns |
| Semi-Supervised Learning | Few labels + many unlabeled | Improve learning efficiency |
| Reinforcement Learning | Interaction with environment | Maximize reward |
