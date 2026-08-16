# Naive Bayes - Complete Notes

# Naive Bayes

## Definition

Naive Bayes is a **supervised machine learning classification algorithm** based on **Bayes' Theorem**. It predicts the class of a data sample by calculating probabilities.

It is called **"Naive"** because it assumes that all features are **independent** of each other.

---

# Bayes' Theorem

[
P(C|X)=\frac{P(X|C)\times P(C)}{P(X)}
]

### Meaning

* **P(C|X)** → Posterior Probability (Probability of class after seeing data)
* **P(X|C)** → Likelihood (Probability of data given the class)
* **P(C)** → Prior Probability (Initial probability of the class)
* **P(X)** → Evidence (Probability of the data)

---

# Working Steps

1. Collect training data.
2. Calculate prior probability of each class.
3. Calculate likelihood of each feature.
4. Apply Bayes' theorem.
5. Choose the class with the highest probability.

---

# Example

Email Classification

Input:

* Contains "Win"
* Contains "Prize"

Output:

* Spam
* Not Spam

Naive Bayes calculates the probability of both classes and predicts the one with the higher probability.

---

# Types of Naive Bayes

### 1. Gaussian Naive Bayes

* Used for continuous numerical data.
* Example: Height, Weight, Temperature

### 2. Multinomial Naive Bayes

* Used for count/frequency data.
* Example: Word count in text classification.

### 3. Bernoulli Naive Bayes

* Used for binary data (0/1, Yes/No).
* Example: Word present or absent.

---

# Advantages

* Simple and fast
* Easy to implement
* Works well on small datasets
* Good for text classification
* Handles multiple classes
* Less training data required

---

# Disadvantages

* Assumes feature independence
* Accuracy decreases if features are highly related
* Zero-frequency problem (solved using Laplace Smoothing)

---

# Applications

* Email Spam Detection
* Sentiment Analysis
* Document Classification
* Medical Diagnosis
* Recommendation Systems
* News Classification

---

# Important Terms

| Term                  | Meaning                             |
| --------------------- | ----------------------------------- |
| Prior Probability     | Initial probability of a class      |
| Likelihood            | Probability of features given class |
| Posterior Probability | Final predicted probability         |
| Evidence              | Probability of input data           |

---

# Short Exam Definition

**Naive Bayes** is a supervised classification algorithm based on Bayes' Theorem that assumes all input features are independent and predicts the class with the highest probability.

---
# Viva Questions

### What is Naive Bayes?

A supervised classification algorithm based on Bayes' Theorem.

### Why is it called "Naive"?

Because it assumes all features are independent.

### Is Naive Bayes supervised or unsupervised?

Supervised.

### Main use?

Classification.

### Which theorem is used?

Bayes' Theorem.

### Types?

* Gaussian
* Multinomial
* Bernoulli

### One real-life application?

Spam email detection.

---
# One-Line Revision

* Algorithm: Supervised Classification
* Based on: Bayes' Theorem
* Assumption: Features are Independent
* Output: Predicted Class
* Best For: Text Classification & Spam Detection
* Types: Gaussian, Multinomial, Bernoulli
