# Utils - ML Engineering Learning Modules

## Overview
This folder contains reusable utility modules built for learning and experimenting with core Machine Learning workflows.  
It is focused on understanding how an end-to-end ML pipeline is structured, including preprocessing, training, evaluation, and feature engineering.

This is a **learning and experimental codebase**, not a production library.

---

## Folder Structure

### Core Pipeline Modules

- **data_loader.py**
  Handles dataset loading and basic input pipeline setup.

- **data_preprocessing.py**
  Implements preprocessing utilities such as:
  - Missing value handling
  - Data cleaning utilities
  - Basic transformations

- **preprocessing.py**
  Extended preprocessing logic including:
  - Duplicate removal
  - Feature preparation workflows

- **feature_engineering.py**
  Feature creation and transformation logic:
  - Encoding strategies
  - Interaction features

---

### Training & Model Workflow

- **model_training.py**
  Training pipeline logic for ML models.

- **training.py**
  Higher-level training orchestration and workflow control.

- **model_utils.py**
  Helper functions related to model handling and reusable training utilities.

---

### Evaluation

- **evaluation.py**
  Model evaluation logic for:
  - Predictions
  - Performance metrics
  - Edge-case handling (e.g., 1D outputs, probability outputs)

---

### General Utilities

- **utils.py**
  Common helper functions including logging and reusable generic utilities.

---

## Purpose of This Module
- Understand ML pipeline architecture step by step
- Experiment with reusable ML components
- Build intuition for production-style ML code structure
- Practice clean separation of concerns in ML systems

---

## Important Note
This repository is:
- For learning and experimentation only
- Frequently changing and not version-stable
- Not intended as a pip-installable package or production framework

---

## Contribution Note
External contributions are welcome only if they improve learning clarity, robustness, or correctness of ML workflows.