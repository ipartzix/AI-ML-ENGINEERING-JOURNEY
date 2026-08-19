# IMDb Movie Review Sentiment Analysis

A Natural Language Processing (NLP) project that performs **binary sentiment classification** on the IMDb Movie Reviews dataset using three different **Naive Bayes classifiers**.

## Dataset

**IMDb Dataset of 50K Movie Reviews**

The dataset contains **50,000 movie reviews** for binary sentiment classification:

- **25,000 positive reviews**
- **25,000 negative reviews**

Dataset: [IMDb Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

The original Large Movie Review Dataset was introduced by Andrew L. Maas et al. at Stanford University.

## Objective

The main objective of this project is to classify movie reviews as either:

- `Positive`
- `Negative`

using different variants of the **Naive Bayes algorithm** and compare their performance.

## Workflow

```text
IMDb Movie Reviews
        ↓
Data Loading
        ↓
Text Cleaning
        ↓
HTML Tag Removal
        ↓
Text Preprocessing
        ↓
Feature Extraction / Vectorization
        ↓
Train-Test Split
        ↓
Naive Bayes Models
        ↓
Predictions
        ↓
Accuracy Evaluation
        ↓
Model Comparison

```

## Naive Bayes Models

### 1. Bernoulli Naive Bayes

Bernoulli Naive Bayes is designed for binary features, where each feature represents whether a word is present or absent in a review.

**Accuracy: 81.94%**

---

### 2. Multinomial Naive Bayes

Multinomial Naive Bayes is commonly used for text classification and works well with word-count-based features.

**Accuracy: 81.41%**

---

### 3. Gaussian Naive Bayes

Gaussian Naive Bayes assumes that the features follow a Gaussian (normal) distribution.

**Accuracy: 78.98%**

---

## Accuracy Comparison

| Naive Bayes Algorithm | Accuracy |
|---|---:|
| **Bernoulli Naive Bayes** | **81.94%** |
| **Multinomial Naive Bayes** | **81.41%** |
| **Gaussian Naive Bayes** | **78.98%** |

### Best Performing Model

```
Bernoulli Naive Bayes — 81.94%
```