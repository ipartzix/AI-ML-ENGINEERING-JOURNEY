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

