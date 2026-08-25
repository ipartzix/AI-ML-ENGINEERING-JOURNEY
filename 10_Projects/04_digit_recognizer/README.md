# Digit Recognizer

A handwritten digit classification project using the **Decision Tree** algorithm on the [Kaggle Digit Recognizer](https://www.kaggle.com/c/digit-recognizer) dataset.

## About

The dataset contains handwritten digits from `0` to `9`. Each image is a **28 × 28 grayscale image**, represented by **784 pixel features**.

The goal of this project is to train a **Decision Tree Classifier** to recognize handwritten digits.

```text
28 × 28 Image
      ↓
784 Pixel Features
      ↓
Preprocessing
      ↓
Decision Tree Classifier
      ↓
Predicted Digit (0–9)