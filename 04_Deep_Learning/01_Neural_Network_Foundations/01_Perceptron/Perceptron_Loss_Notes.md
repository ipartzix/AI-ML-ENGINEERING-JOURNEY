# Perceptron Loss, Hinge Loss, Binary Cross-Entropy & Sigmoid

## 1. Overview

A classification model needs a way to measure how wrong its prediction
is. This is the role of a **loss function**.

The progression covered here is:

**Perceptron → Perceptron Loss → Gradient Descent → Hinge Loss → Sigmoid
→ Binary Cross-Entropy**

## 2. Perceptron Recap

A perceptron computes:

`z = wᵀx + b`

For labels `y ∈ {-1, +1}`:

`ŷ = sign(wᵀx + b)`

The decision boundary is:

`wᵀx + b = 0`

## 3. Perceptron Trick

For a misclassified example:

`w ← w + ηyx`

`b ← b + ηy`

where `η` is the learning rate.

The basic perceptron update tells us whether a point is correctly
classified or not, but it does not provide a smooth measure of the
prediction error. A loss function gives us an explicit objective to
minimize.

## 4. Loss Function

A loss function measures the error for an individual training example:

`L(y, ŷ)`

The average training objective is:

`J(w,b) = (1/n) Σ Lᵢ`

-   **Loss:** error for one example.
-   **Cost:** aggregate loss over the dataset.

## 5. Perceptron Loss

For `y ∈ {-1,+1}` and score `z = wᵀx+b`:

`L(y,z) = max(0, -yz)`

The quantity `yz` is important:

-   `yz > 0` → correctly classified.
-   `yz < 0` → incorrectly classified.
-   Larger positive `yz` → stronger correct classification.
-   Negative `yz` → wrong classification.

Therefore:

`L = max(0, -yz)`

### Examples

For `y = +1, z = 3`:

`L = max(0,-3) = 0`

For `y = +1, z = -2`:

`L = max(0,2) = 2`

So correct classification receives zero loss, while misclassification
receives positive loss.

## 6. Geometric Intuition

The decision boundary is:

`wᵀx+b = 0`

Perceptron loss is connected to which side of the decision boundary the
point lies on and how strongly the signed score indicates a mistake.

Unlike a simple correct/incorrect indicator, the loss also reflects the
severity of a misclassification.

## 7. Gradient Descent

After defining a loss, an optimization method is required to minimize
it.

`θ ← θ - η∇θJ(θ)`

Basic process:

``` text
Initialize parameters
        ↓
Calculate score/prediction
        ↓
Calculate loss
        ↓
Calculate gradient
        ↓
Update parameters
        ↓
Repeat
```

For a misclassified perceptron example:

`L = -y(wᵀx+b)`

The gradients are:

`∂L/∂w = -yx`

`∂L/∂b = -y`

Gradient descent therefore gives:

`w ← w + ηyx`

`b ← b + ηy`

This connects the classical perceptron update with loss minimization.

## 8. Hinge Loss

Hinge loss is strongly associated with Support Vector Machines.

For `y ∈ {-1,+1}`:

`L(y,z) = max(0, 1-yz)`

Compare:

**Perceptron loss**

`L = max(0,-yz)`

**Hinge loss**

`L = max(0,1-yz)`

The key difference is the **margin of 1**.

## 9. Perceptron Loss vs Hinge Loss

Perceptron loss gives zero loss whenever the example is on the correct
side of the boundary.

Hinge loss gives zero loss only when:

`yz ≥ 1`

Therefore, hinge loss encourages a margin between classes.

    Score `z` for `y=+1`   Perceptron Loss   Hinge Loss
  ---------------------- ----------------- ------------
                      -2                 2            3
                    -0.5               0.5          1.5
                       0                 0            1
                     0.5                 0          0.5
                       1                 0            0
                       2                 0            0

### Key difference

**Perceptron loss:** correct side is enough.

**Hinge loss:** correct side + sufficient margin.

## 10. Why Margin Matters

Suppose two points are correctly classified:

-   Point A: `yz = 0.2`
-   Point B: `yz = 3`

Perceptron loss gives both zero loss.

Hinge loss gives:

`L_A = 0.8`

`L_B = 0`

Therefore hinge loss continues penalizing correctly classified points
when they are too close to the decision boundary.

## 11. Sigmoid Function

For binary classification, a linear score can be converted into a value
between 0 and 1:

`σ(z) = 1 / (1 + e⁻ᶻ)`

Properties:

-   `z → +∞` → `σ(z) → 1`
-   `z = 0` → `σ(z) = 0.5`
-   `z → -∞` → `σ(z) → 0`

The output can be interpreted as the model's probability estimate for
the positive class.

## 12. Sigmoid + Linear Model

First calculate:

`z = wᵀx+b`

Then:

`p = σ(z)`

So:

`p = P(y=1|x)`

A common decision rule is:

-   `p ≥ 0.5` → class 1
-   `p < 0.5` → class 0

Because `σ(0)=0.5`, the classification boundary corresponds to:

`wᵀx+b = 0`

## 13. Binary Cross-Entropy

Binary Cross-Entropy (BCE), also called log loss, is commonly used for
binary classification with probabilistic outputs.

For `y ∈ {0,1}` and predicted probability `p`:

`L = -[y log(p) + (1-y) log(1-p)]`

### When `y = 1`

`L = -log(p)`

So:

-   `p → 1` → very small loss.
-   `p → 0` → very large loss.

### When `y = 0`

`L = -log(1-p)`

So:

-   `p → 0` → very small loss.
-   `p → 1` → very large loss.

The important idea is:

> BCE rewards correct confidence and heavily penalizes confident
> incorrect predictions.

## 14. BCE Intuition

For `y=1`:

    Predicted probability Loss behavior
  ----------------------- ---------------
                     0.99 Very small
                     0.90 Small
                     0.60 Moderate
                     0.10 Large
                     0.01 Very large

For `y=0`, the behavior is reversed.

## 15. Why Sigmoid and BCE Are Used Together

A common binary-classification model is:

`z = wᵀx+b`

`p = σ(z)`

`L = -[y log(p)+(1-y)log(1-p)]`

Their gradient with respect to the logit simplifies to:

`∂L/∂z = p-y`

In practical deep-learning frameworks, a numerically stable combined
implementation is preferred.

PyTorch provides:

``` python
torch.nn.BCEWithLogitsLoss()
```

This combines the sigmoid operation and binary cross-entropy in a
numerically stable way.

## 16. Perceptron Loss vs Hinge Loss vs BCE

  -----------------------------------------------------------------------
  Property          Perceptron Loss   Hinge Loss        Binary
                                                        Cross-Entropy
  ----------------- ----------------- ----------------- -----------------
  Typical labels    `-1,+1`           `-1,+1`           `0,1`

  Uses probability  No                No                Yes

  Typical model     Perceptron        SVM               Logistic
                                                        regression /
                                                        neural network

  Margin            No                Yes               No explicit
                                                        margin

  Smooth            No                No                Yes

  Penalizes         Yes               Yes               Strongly
  confident wrong                                       
  prediction                                            

  Zero loss for     Yes               Yes, margin ≥ 1   No
  sufficiently                                          
  correct                                               
  prediction                                            
  -----------------------------------------------------------------------

## 17. Core Mathematical Difference

### Perceptron Loss

`L = max(0,-yz)`

**Goal:** classify the point on the correct side.

### Hinge Loss

`L = max(0,1-yz)`

**Goal:** classify correctly with a margin.

### Binary Cross-Entropy

`L = -[y log(p)+(1-y)log(1-p)]`

**Goal:** learn accurate probabilistic predictions.

## 18. Relationship Between the Concepts

``` text
Linear score
    │
    ├── z = wᵀx + b
    │
    ├── Perceptron Loss
    │       └── Correct side of boundary
    │
    ├── Hinge Loss
    │       └── Correct side + margin
    │
    └── Sigmoid
            └── Score → probability
                    │
                    └── Binary Cross-Entropy
                            └── Probability error
```

## 19. Important Practical Distinction

### Perceptron

A **model/algorithm** for linear classification.

### Sigmoid

A **function** that maps a real-valued score to `(0,1)`.

### Perceptron Loss

A **loss function** based on the signed classification score.

### Hinge Loss

A **margin-based loss**, strongly associated with SVMs.

### Binary Cross-Entropy

A **probabilistic classification loss** commonly used with sigmoid
outputs.

### Gradient Descent

An **optimization algorithm** used to minimize a loss.

## 20. Scikit-Learn Perspective

Common binary classification models include:

``` python
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
```

Conceptually:

``` text
Perceptron
    → Perceptron-style learning

Logistic Regression
    → Sigmoid + log loss / BCE

SVM
    → Margin-based learning + hinge-loss concept
```

Implementations can also include regularization and other optimization
details.

## 21. Interview Questions

### Q1. What is perceptron loss?

`L = max(0,-yz)`

It gives zero loss to correctly classified points and positive loss to
misclassified points.

### Q2. Difference between perceptron loss and hinge loss?

Perceptron loss requires correct classification. Hinge loss additionally
encourages a margin.

### Q3. Why is hinge loss used with SVM?

Because SVM aims to find a decision boundary with a large margin, and
hinge loss penalizes violations of that margin.

### Q4. Why is sigmoid used in binary classification?

It converts a real-valued score into a value between 0 and 1 that can be
interpreted as a probability estimate.

### Q5. What is BCE?

`L = -[y log(p)+(1-y)log(1-p)]`

It measures the error between the true binary label and predicted
probability.

### Q6. Why does BCE penalize confident wrong predictions strongly?

Because the logarithmic loss becomes very large when the predicted
probability assigned to the true class approaches zero.

### Q7. Loss vs gradient descent?

The **loss defines what should be minimized**. Gradient descent defines
**how parameters are updated to minimize it**.

### Q8. Why use `BCEWithLogitsLoss`?

It combines the sigmoid and BCE calculation in a numerically stable
implementation.

## 22. Final Mental Model

``` text
Perceptron
    ↓
Linear score: z = wᵀx + b
    ↓
Need a measurable objective
    ↓
Perceptron Loss
    ↓
Gradient Descent
    ↓
Margin-based learning
    ↓
Hinge Loss
    ↓
Probabilistic binary classification
    ↓
Sigmoid
    ↓
Binary Cross-Entropy
```

### One-line summary

> **Perceptron loss cares about being on the correct side, hinge loss
> cares about being on the correct side with a margin, and BCE cares
> about producing accurate probabilities.**
