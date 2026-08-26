# Ensemble Learning

## 1. What is Ensemble Learning?

**Ensemble Learning** is a machine learning technique where multiple machine learning models are combined to produce a stronger and more reliable model.

Instead of depending on one model, ensemble learning combines the predictions of multiple models, called **base learners**, to make the final prediction.

> **The main idea of ensemble learning is to combine multiple models so that their combined prediction is better than the prediction of an individual model.**

### Why Use Ensemble Learning?

Ensemble learning can help to:

- Improve prediction accuracy
- Improve generalization
- Reduce variance
- Reduce bias
- Reduce overfitting
- Improve model stability
- Improve robustness
- Combine the strengths of different models

---

# 2. Types of Ensemble Learning

The four major types of ensemble learning are:

1. **Voting**
2. **Bagging**
3. **Boosting**
4. **Stacking**

```

                         Ensemble Learning
                                |
        +-----------+-----------+-----------+-----------+
        |           |                       |           |
        v           v                       v           v
     Voting      Bagging                Boosting    Stacking
        |           |                       |           |
        v           v                       v           v
  Predictions  Bootstrap              Sequential   Base Learners
               Samples                  Models          |
                   |                       |            v
             +-----+-----+          +------+------+  Predictions
             |           |          |      |      |
             v           v          v      v      v
       Random Forest  Extra Trees AdaBoost XGBoost LightGBM
                                                       |
                                                       v
                                                    CatBoost

Stacking:
Base Learners → Predictions → Meta-Learner → Final Prediction
```