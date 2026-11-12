# Loss Functions in Deep Learning

Loss functions measure the difference between a model's predictions and
the actual target values. The appropriate loss function depends on the
learning task.

## 1. Regression Loss Functions

Regression models predict continuous numerical values. Their loss
functions measure the numerical distance between actual and predicted
values.

### 1.1 Mean Squared Error (MSE / L2 Loss)

Calculates the average of the squared differences between actual and
predicted values.

\[ `\text{MSE}`{=tex} =
`\frac{1}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}(y_i-`\hat{y}`{=tex}\_i)\^2
\]

-   (n): Number of samples
-   (y_i): Actual value
-   (`\hat{y}`{=tex}\_i): Predicted value

**Key point:** Squaring the errors penalizes larger errors more heavily,
making MSE sensitive to outliers.

**Sources:** [Google Machine Learning Crash
Course](https://developers.google.com/machine-learning/crash-course/linear-regression/loss)
·
[GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/loss-functions-in-deep-learning/)
· [Related research article](https://arxiv.org/html/2504.04242v1)

### 1.2 Mean Absolute Error (MAE / L1 Loss)

Measures the average of the absolute differences between actual and
predicted values. It is less sensitive to outliers than MSE.

\[ `\text{MAE}`{=tex} =
`\frac{1}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}\|y_i-`\hat{y}`{=tex}\_i\| \]

**Key point:** MAE penalizes errors linearly rather than squaring them.

**Sources:**
[GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/loss-functions-in-deep-learning/)
· [Google Machine Learning Crash
Course](https://developers.google.com/machine-learning/crash-course/linear-regression/loss)

### 1.3 Huber Loss

Huber Loss combines the behavior of MSE and MAE. It is quadratic for
small errors and linear for large errors beyond a threshold
(`\delta`{=tex}).

\[ L\_{`\delta`{=tex}}(y,`\hat{y}`{=tex}) =
```{=tex}
\begin{cases}
\frac{1}{2}(y-\hat{y})^2,
& \text{if } |y-\hat{y}|\leq\delta \\[6pt]
\delta\left(|y-\hat{y}|-\frac{1}{2}\delta\right),
& \text{otherwise}
\end{cases}
```
\]

-   (`\delta`{=tex}): Threshold that determines the transition between
    quadratic and linear behavior.

**Key point:** Huber Loss is less sensitive to large errors than MSE
while retaining a smooth quadratic region around zero.

**Source:** [Loss Functions in Deep Learning ---
Medium](https://medium.com/@ibtedaazeem/loss-functions-in-deep-learning-e4bd353ea08a)

------------------------------------------------------------------------

## 2. Classification Loss Functions

Classification models predict categories. Their loss functions measure
how well the predicted outputs agree with the true class labels.
Cross-entropy losses penalize predictions that assign low probability to
the correct class.

### 2.1 Binary Cross-Entropy (BCE / Log Loss)

Used for binary classification tasks where the true label is
(y_i`\in`{=tex}{0,1}), and (`\hat{y}`{=tex}\_i) is the predicted
probability of class 1.

\[ `\text{BCE}`{=tex} = -`\frac{1}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}
`\left[
y_i\log(\hat{y}_i)
+(1-y_i)\log(1-\hat{y}_i)
\right]`{=tex}\]

**Key point:** BCE is used when each prediction represents a binary
target.

**Sources:** [Binary Cross-Entropy
explanation](https://www.youtube.com/watch?v=M0uABtRKDmA) ·
[GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/loss-functions-in-deep-learning/)

### 2.2 Categorical Cross-Entropy (CCE)

Used for multiclass classification across (k) categories when the true
labels are represented using one-hot encoding.

\[ `\text{CCE}`{=tex} =
-`\frac{1}{n}`{=tex}`\sum`{=tex}*{i=1}\^{n}`\sum`{=tex}*{j=1}\^{k}
y\_{ij}`\log`{=tex}(`\hat{y}`{=tex}\_{ij}) \]

-   (n): Number of samples
-   (k): Number of classes
-   (y\_{ij}): Actual one-hot encoded label for sample (i), class (j)
-   (`\hat{y}`{=tex}\_{ij}): Predicted probability for sample (i), class
    (j)

**Key point:** CCE is commonly used when each sample belongs to exactly
one of multiple classes.

**Sources:**
[GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/loss-functions-in-deep-learning/)
· [Loss functions
explanation](https://www.youtube.com/watch?v=c6HrNJPY2EM&t=354)

### 2.3 Hinge Loss

Primarily used for maximum-margin classification, such as Support Vector
Machines (SVMs). The labels are represented as (y_i`\in`{=tex}{-1,+1}).

\[ `\text{Hinge Loss}`{=tex} =
`\frac{1}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}
`\max`{=tex}(0,1-y_i`\hat{y}`{=tex}\_i) \]

Here, (`\hat{y}`{=tex}\_i) represents the model's prediction score, not
a probability.

**Key point:** Hinge Loss penalizes predictions that are incorrect or
that do not satisfy the required classification margin.

**Source:**
[GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/loss-functions-in-deep-learning/)

------------------------------------------------------------------------

## 3. Quick Comparison

  -----------------------------------------------------------------------
  Loss function           Task                    Main characteristic
  ----------------------- ----------------------- -----------------------
  MSE / L2                Regression              Squares errors;
                                                  sensitive to outliers

  MAE / L1                Regression              Uses absolute errors;
                                                  less sensitive to
                                                  outliers

  Huber                   Regression              Quadratic for small
                                                  errors, linear for
                                                  large errors

  Binary Cross-Entropy    Binary classification   Measures error in
                                                  predicted binary
                                                  probabilities

  Categorical             Multiclass              Measures error in
  Cross-Entropy           classification          predicted class
                                                  probabilities

  Hinge Loss              Margin-based            Encourages correct
                          classification          predictions with a
                                                  classification margin
  -----------------------------------------------------------------------

## 4. Important Notes

1.  MSE and MAE are regression losses, while BCE and CCE are commonly
    used for classification.
2.  Huber Loss combines properties of squared-error and absolute-error
    losses.
3.  Hinge Loss uses class labels of (-1) and (+1) in its standard
    formulation.
4.  The meaning of (`\hat{y}`{=tex}) depends on the loss function: it
    may be a numerical prediction, a probability, or a prediction score.
5.  Choose a loss function according to the task and the representation
    of the model's output and target labels.

## 5. Self-Assessment

1.  Why is MSE more sensitive to outliers than MAE?
2.  What is the difference between L1 and L2 Loss?
3.  How does Huber Loss combine MSE and MAE?
4.  When should Binary Cross-Entropy be used?
5.  What is the role of one-hot encoding in Categorical Cross-Entropy?
6.  How is Hinge Loss different from Cross-Entropy?

------------------------------------------------------------------------

**Repository location:**

`04_Deep_Learning/01_Neural_Network_Foundations/05_Loss_Functions/README.md`
