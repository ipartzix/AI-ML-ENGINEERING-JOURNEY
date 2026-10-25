# Gradient Descent

> **Purpose:** Understand how a model learns its parameters by
> minimizing a loss function.

## 1. What Is Gradient Descent?

**Gradient Descent** is an iterative optimization algorithm used to find
parameter values that minimize an objective function, such as a
machine-learning model's loss.

A model makes predictions using parameters (weights and biases). The
loss function measures how far those predictions are from the target
values. Gradient descent updates the parameters in the direction that
reduces the loss.

It is used in linear and logistic regression, neural networks, and many
other machine-learning algorithms.

## 2. Core Intuition

Imagine the loss function as a landscape:

-   The **height** represents the loss.
-   The **current position** represents the current parameter values.
-   The **slope** indicates how the loss changes as a parameter changes.
-   The algorithm takes repeated steps toward lower loss.

The gradient points in the direction of the steepest local increase.
Therefore, gradient descent moves in the **negative-gradient
direction**.

## 3. Mathematical Formulation

Let:

-   (`\theta`{=tex}) represent the model parameters.
-   (J(`\theta`{=tex})) represent the objective or loss function.
-   (`\eta`{=tex}) represent the learning rate.
-   (`\nabla`{=tex}\_`\theta `{=tex}J(`\theta`{=tex})) represent the
    gradient of the loss with respect to the parameters.

The update rule is:

\[ `\theta`{=tex}\_{t+1} = `\theta`{=tex}*t -
`\eta `{=tex}`\nabla`{=tex}*`\theta `{=tex}J(`\theta`{=tex}\_t) \]

For a single parameter (w):

\[ w\_{t+1} = w_t - `\eta `{=tex}`\frac{\partial J}{\partial w}`{=tex}
\]

For a model with weights and bias:

\[ w\_{t+1} = w_t - `\eta `{=tex}`\frac{\partial J}{\partial w}`{=tex}
\]

\[ b\_{t+1} = b_t - `\eta `{=tex}`\frac{\partial J}{\partial b}`{=tex}
\]

**Interpretation:** Calculate how the loss changes with each parameter,
then adjust each parameter in the opposite direction, scaled by the
learning rate.

## 4. How Gradient Descent Works

1.  **Initialize parameters** --- choose initial weights and biases.
2.  **Make predictions** --- run the model using the current parameters.
3.  **Calculate the loss** --- measure prediction error with an
    objective function.
4.  **Calculate gradients** --- determine the partial derivative of the
    loss with respect to each parameter.
5.  **Update parameters** --- subtract the learning-rate-scaled
    gradients.
6.  **Repeat** --- continue until a stopping condition is reached.

A training iteration is often called a **step**. In mini-batch training,
one epoch usually means processing all training examples once.

## 5. Example: Minimize a Simple Function

Consider:

\[ J(w) = (w - 3)\^2 \]

Its derivative is:

\[ `\frac{dJ}{dw}`{=tex} = 2(w - 3) \]

Using (w_0 = 0) and learning rate (`\eta `{=tex}= 0.1):

\[ w_1 = 0 - 0.1\[2(0 - 3)\] = 0.6 \]

The new value is closer to (3), the minimizer of this function.
Repeating the update moves (w) toward (3).

This is a one-dimensional example. Real models generally have many
parameters and use gradients computed from a dataset.

## 6. Types of Gradient Descent

  ------------------------------------------------------------------------
  Type              Data used for     Advantages        Limitations
                    each update                         
  ----------------- ----------------- ----------------- ------------------
  **Batch Gradient  Entire training   Stable,           Can be slow and
  Descent**         dataset           relatively smooth memory-intensive
                                      gradient          on large datasets
                                      estimates         

  **Stochastic      One training      Frequent updates; Noisy updates;
  Gradient Descent  example           useful for large  loss may fluctuate
  (SGD)**                             or streaming      
                                      datasets          

  **Mini-Batch      A small batch of  Efficient         Requires choosing
  Gradient          examples          vectorized        a batch size
  Descent**                           computation;      
                                      balances noise    
                                      and stability     
  ------------------------------------------------------------------------

### Batch Gradient Descent

The gradient is calculated using the full training set before each
parameter update. This can be computationally expensive when the dataset
is large.

### Stochastic Gradient Descent (SGD)

The parameters are updated using one training example at a time. Updates
are inexpensive but noisy. The term **SGD** is also commonly used for
mini-batch stochastic optimization in deep-learning libraries.

### Mini-Batch Gradient Descent

The gradient is computed from a subset of the training data. Common
batch sizes include 32, 64, and 128, but the best choice depends on the
model, dataset, and hardware.

## 7. The Learning Rate

The **learning rate** controls the size of each parameter update.

-   **Too small:** training can progress very slowly.
-   **Reasonable:** loss often decreases steadily, although it may not
    decrease on every stochastic step.
-   **Too large:** updates may overshoot a minimum, oscillate, or
    diverge.

The learning rate is a hyperparameter. It is commonly tuned using a
validation set, learning-rate schedules, or adaptive optimizers.

## 8. Convex and Non-Convex Loss Landscapes

-   **Convex objective:** every local minimum is a global minimum. For a
    differentiable convex function, gradient descent can converge to a
    global minimum under suitable conditions.
-   **Non-convex objective:** may contain local minima, saddle points,
    and flat regions. Deep neural-network objectives are generally
    non-convex.

Convergence depends on the objective, learning rate, gradient behavior,
initialization, and stopping criteria. Gradient descent does not
guarantee that every arbitrary training setup will reach a global
minimum.

## 9. Common Problems and Practical Responses

  -----------------------------------------------------------------------
  Problem                 Typical symptom         Possible response
  ----------------------- ----------------------- -----------------------
  Learning rate too high  Loss oscillates or      Reduce the learning
                          becomes `NaN`/diverges  rate; inspect gradient
                                                  and data values

  Learning rate too low   Loss decreases          Try a larger learning
                          extremely slowly        rate or a schedule

  Poor feature scales     Optimization behaves    Standardize or
                          unevenly across         normalize features
                          features                where appropriate

  Noisy updates           Loss fluctuates between Increase batch size,
                          steps                   tune learning rate, or
                                                  average evaluation over
                                                  epochs

  Vanishing gradients     Gradients become very   Review activation
                          small in earlier layers functions,
                                                  initialization, and
                                                  architecture

  Exploding gradients     Gradients become        Consider gradient
                          extremely large         clipping,
                                                  initialization, and
                                                  architecture

  Overfitting             Training loss improves  Use validation
                          but validation          monitoring and
                          performance worsens     appropriate
                                                  regularization
  -----------------------------------------------------------------------

**Important distinction:** Gradient descent is the optimization
procedure. The loss function defines what is being minimized; the model
defines the predictions; and the optimizer's settings control how
parameters are updated.

## 10. NumPy Implementation From Scratch

This example fits a straight line, (`\hat{y}`{=tex} = wx + b), by
minimizing mean squared error (MSE).

``` python
import numpy as np

# Small synthetic dataset: y = 2x + 1
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

# Initialize parameters
w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 1000
n = len(X)

for epoch in range(epochs):
    # Forward pass
    y_pred = w * X + b

    # Mean squared error
    error = y_pred - y
    loss = np.mean(error ** 2)

    # Gradients of MSE with respect to w and b
    dw = (2 / n) * np.sum(error * X)
    db = (2 / n) * np.sum(error)

    # Gradient descent update
    w -= learning_rate * dw
    b -= learning_rate * db

    if (epoch + 1) % 100 == 0:
        print(
            f"Epoch {epoch + 1:4d} | "
            f"Loss: {loss:.6f} | w: {w:.4f} | b: {b:.4f}"
        )

print(f"\nLearned equation: y = {w:.3f}x + {b:.3f}")
```

The learned values should approach (w=2) and (b=1). The loss printed
inside the loop is calculated before that iteration's update.

### Why are the gradients calculated this way?

For mean squared error,

\[ J(w,b) = `\frac{1}{n}`{=tex}`\sum`{=tex}\_{i=1}^{n}(wx_i+b-y_i)^2 \]

The partial derivatives are:

\[ `\frac{\partial J}{\partial w}`{=tex} =
`\frac{2}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}(wx_i+b-y_i)x_i \]

\[ `\frac{\partial J}{\partial b}`{=tex} =
`\frac{2}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}(wx_i+b-y_i) \]

These derivatives measure how the MSE changes when (w) or (b) changes.
They are then used in the gradient-descent update rule.

## 11. Gradient Descent vs. Optimizers

Gradient descent describes the general idea of updating parameters using
gradients. Practical libraries provide optimizers that modify or extend
this idea.

-   **SGD:** uses gradient-based updates, optionally with momentum.
-   **Momentum:** uses a running direction to reduce some oscillations
    and accelerate progress in consistent directions.
-   **RMSprop:** adapts update scales using a moving average of squared
    gradients.
-   **Adam:** combines momentum-like first-moment estimates with
    adaptive second-moment estimates.

Adam and RMSprop are adaptive gradient-based optimizers; they are not
identical to plain gradient descent.

## 12. Gradient Descent vs. Backpropagation

These concepts are related but different:

-   **Backpropagation** computes gradients of a neural network's loss
    with respect to its parameters by applying the chain rule.
-   **Gradient descent** uses gradients to update the parameters.

In a neural network, backpropagation usually calculates the gradients;
an optimizer such as SGD or Adam uses them to perform the update.

## 13. Key Takeaways

-   Gradient descent minimizes a differentiable objective by moving
    parameters opposite the gradient.
-   The learning rate controls update size and strongly affects
    training.
-   Batch, stochastic, and mini-batch variants differ in how much data
    is used to estimate each update.
-   Feature scaling and sensible optimization settings can improve
    training.
-   Backpropagation computes neural-network gradients; an optimizer
    applies parameter updates.
-   Monitor both training and validation metrics rather than assuming
    lower training loss always means a better model.

## 14. Quick Self-Check

1.  Why does gradient descent subtract the gradient instead of adding
    it?
2.  What can happen if the learning rate is too large?
3.  How does mini-batch gradient descent differ from batch gradient
    descent?
4.  What is the difference between backpropagation and gradient descent?
5.  Why might training loss decrease while validation performance gets
    worse?

------------------------------------------------------------------------

