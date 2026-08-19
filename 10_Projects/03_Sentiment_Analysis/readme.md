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