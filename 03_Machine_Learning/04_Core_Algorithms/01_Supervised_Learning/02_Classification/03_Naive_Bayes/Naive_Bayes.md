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

# Types of Naive Bayes

### 1. Gaussian Naive Bayes

* **Overview:** Used when input features are **continuous numerical values** (e.g., age, salary, height, blood pressure). Instead of counting frequencies, it assumes that continuous values associated with each class follow a **Gaussian (Normal) Distribution** (bell curve).
* **Mathematical Likelihood Formula:**

  $$P(x_i | C_k) = \frac{1}{\sqrt{2\pi\sigma_k^2}} \exp\left( -\frac{(x_i - \mu_k)^2}{2\sigma_k^2} \right)$$

  * $\mu_k$ = Mean of feature $x_i$ for class $C_k$
  * $\sigma_k^2$ = Variance of feature $x_i$ for class $C_k$

* **Key Characteristics:**
  * Does not require discretization or binning of continuous data.
  * Calculates mean ($\mu$) and variance ($\sigma^2$) for each feature per class during training.
  * Sensitive to extreme outliers because outliers significantly distort the calculated mean and variance.

* **Best Use Cases:**
  * Predicting disease presence using clinical vital metrics (blood pressure, heart rate, cholesterol levels).
  * Weather prediction based on temperature, humidity, and atmospheric pressure.

---

### 2. Multinomial Naive Bayes

* **Overview:** Designed for **discrete count data**. It models the probability of feature occurrences based on their frequencies. It is the most popular variant for Natural Language Processing (NLP) tasks using bag-of-words or term-frequency (TF) representations.
* **Mathematical Likelihood Formula:**

  $$P(X | C_k) = \frac{(\sum_i x_i)!}{\prod_i x_i!} \prod_i P(w_i | C_k)^{x_i}$$

  For individual word/term likelihoods with **Laplace Smoothing ($ lpha = 1$)**:

  $$P(w_i | C_k) = \frac{N_{k,i} + \alpha}{N_k + \alpha \cdot |V|}$$

  * $N_{k,i}$ = Count of word $i$ appearing in class $C_k$
  * $N_k$ = Total count of all words in class $C_k$
  * $|V|$ = Vocabulary size (total unique words across all classes)
  * $\alpha$ = Smoothing parameter (prevents zero-probability issues)

* **Key Characteristics:**
  * Accounts for word frequency (e.g., the word "free" appearing 5 times carries more weight than appearing once).
  * Handles high-dimensional, sparse matrix data efficiently.

* **Best Use Cases:**
  * Document classification (e.g., tagging news articles as Sports, Politics, or Tech).
  * Spam detection using Term Frequency (TF) or TF-IDF representations.

---

### 3. Bernoulli Naive Bayes

* **Overview:** Used when features are **binary variables** (0 or 1, True or False, Present or Absent). Unlike Multinomial Naive Bayes, it does not care *how many times* a feature occurs—only *whether* it occurs.
* **Mathematical Likelihood Formula:**

  $$P(X | C_k) = \prod_{i=1}^{n} P(i | C_k)^{x_i} \cdot (1 - P(i | C_k))^{(1 - x_i)}$$

  * $x_i \in \{0, 1\}$ represents the absence or presence of feature $i$.
  * $P(i | C_k)$ = Probability of feature $i$ occurring in class $C_k$.

* **Key Characteristics:**
  * Penalizes the non-occurrence of a feature (the term $(1 - P(i|C_k))$ explicitly accounts for absent features).
  * Best suited for short texts where word repetition is minimal or irrelevant.

* **Best Use Cases:**
  * Short text classification (e.g., sentiment analysis on short tweets or customer reviews using binary presence vectors).
  * Detection of specific binary traits (e.g., check-list responses: Has Fever = 1, Has Cough = 0).

---

# Summary Comparison

| Feature | Gaussian Naive Bayes | Multinomial Naive Bayes | Bernoulli Naive Bayes |
| :--- | :--- | :--- | :--- |
| **Data Type** | Continuous / Real-valued | Discrete Counts | Binary (0 / 1) |
| **Key Metric** | Mean & Variance ($\mu, \sigma^2$) | Feature Frequencies / Counts | Presence or Absence |
| **Penalizes Absence?** | N/A | No | Yes |
| **Primary Domain** | Sensor / Scientific Data | Document & Text Mining | Short Text & Binary Surveys |
