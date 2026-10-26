# Weight Initialization

> **Purpose:** Understand how neural-network weights should be
> initialized to support stable and effective training.

## 1. What Is Weight Initialization?

**Weight initialization** is the process of assigning initial values to
a neural network's trainable parameters before training begins.

Neural networks learn by updating weights and biases using gradients.
The initial parameter values influence the activations, gradient
magnitudes, and speed and stability of optimization.

A suitable initialization helps preserve signal and gradient scales
across layers. A poor initialization can make training slow or unstable.

## 2. Why Initialization Matters

### 2.1 Avoiding Symmetry

If every neuron in a layer starts with exactly the same weights, neurons
can produce the same outputs and receive the same gradients. They may
therefore learn identical features instead of developing distinct
representations.

For hidden-layer weights, random initialization helps break this
symmetry.

**Important:** Randomness alone is not enough. The scale of the initial
weights also matters.

### 2.2 Maintaining Activation and Gradient Scales

As information passes through many layers, activations and gradients can
become progressively smaller or larger.

-   **Vanishing gradients:** gradients become very small, making earlier
    layers learn slowly.
-   **Exploding gradients:** gradients become very large, potentially
    causing unstable updates.

An initialization method should be chosen with the network architecture
and activation functions in mind to help maintain appropriate scales.

### 2.3 Improving Optimization

A suitable initialization can make optimization more stable and reduce
the time required for training to make useful progress. It does not
guarantee convergence or good generalization.

## 3. Common Initialization Strategies

### 3.1 Zero Initialization

All weights are initialized to zero.

**Why it is problematic for hidden-layer weights:** identical neurons
begin with identical parameters, produce identical activations, and
receive identical gradients. This symmetry prevents them from learning
different features.

**Practical guidance:** Do not initialize all weights in a standard
multi-neuron hidden layer to zero.

Biases, however, are often initialized to zero because this does not
create the same symmetry problem when the weights are initialized
appropriately.

### 3.2 Random Initialization

Weights are sampled from a random distribution, often a uniform or
normal distribution.

Random initialization breaks symmetry, but an arbitrary scale may still
be unsuitable. Values that are too large or too small can lead to poor
activation and gradient scales.

Modern initialization methods use the layer's dimensions and, in some
cases, its activation function to choose a more appropriate scale.

### 3.3 Xavier / Glorot Initialization

**Xavier initialization**, also called **Glorot initialization**, is
commonly used with approximately linear or symmetric activations such as
`tanh`.

Let:

-   (n\_{`\text{in}`{=tex}}) be the number of input units to a layer.
-   (n\_{`\text{out}`{=tex}}) be the number of output units.

The Glorot uniform distribution is:

\[ W
`\sim `{=tex}U`\left`{=tex}(-`\sqrt{\frac{6}{n_{\text{in}}+n_{\text{out}}}}`{=tex},
`\sqrt{\frac{6}{n_{\text{in}}+n_{\text{out}}}}`{=tex}`\right`{=tex}) \]

The Glorot normal distribution uses zero-mean weights with variance:

\[
`\operatorname{Var}`{=tex}(W)=`\frac{2}{n_{\text{in}}+n_{\text{out}}}`{=tex}
\]

**Intuition:** It balances the number of input and output units to help
keep signal scales from changing too sharply across layers.

**Typical use:** `tanh`, sigmoid, and other settings where Glorot's
assumptions are appropriate.

### 3.4 He / Kaiming Initialization

**He initialization**, also called **Kaiming initialization**, is
commonly used with ReLU-family activations.

A common normal form is:

\[ W
`\sim `{=tex}`\mathcal{N}`{=tex}`\left`{=tex}(0,`\frac{2}{n_{\text{in}}}`{=tex}`\right`{=tex})
\]

Here, the second parameter shown is the **variance**, not the standard
deviation. Equivalently, the standard deviation is
(`\sqrt{2/n_{\text{in}}}`{=tex}).

A common uniform form is:

\[ W
`\sim `{=tex}U`\left`{=tex}(-`\sqrt{\frac{6}{n_{\text{in}}}}`{=tex},
`\sqrt{\frac{6}{n_{\text{in}}}}`{=tex}`\right`{=tex}) \]

**Intuition:** The scale is chosen to account for the reduction in
active signal associated with ReLU.

**Typical use:** ReLU and related activations, with the exact choice
depending on the activation and framework convention.

### 3.5 LeCun Initialization

LeCun initialization is associated with activations such as SELU and is
designed around preserving activation variance under particular
assumptions.

A common normal form is:

\[ W
`\sim `{=tex}`\mathcal{N}`{=tex}`\left`{=tex}(0,`\frac{1}{n_{\text{in}}}`{=tex}`\right`{=tex})
\]

A common uniform form is:

\[ W
`\sim `{=tex}U`\left`{=tex}(-`\sqrt{\frac{3}{n_{\text{in}}}}`{=tex},
`\sqrt{\frac{3}{n_{\text{in}}}}`{=tex}`\right`{=tex}) \]

**Typical use:** SELU networks often use LeCun normal initialization
together with the other conditions required for self-normalizing
behavior.

## 4. Quick Comparison

  ------------------------------------------------------------------------------------------------------------
  Method            Typical           Common variance or range                               Practical note
                    activation /                                                             
                    setting                                                                  
  ----------------- ----------------- ------------------------------------------------------ -----------------
  Zero weights      Not recommended   All weights equal to zero                              Can prevent
                    for ordinary                                                             hidden neurons
                    hidden-layer                                                             from learning
                    weights                                                                  distinct features

  Random, arbitrary Depends on chosen No single standard formula                             Breaks symmetry
  scale             distribution                                                             but may have
                                                                                             unsuitable scale

  Xavier / Glorot   `tanh`, sigmoid   Variance                                               Balances fan-in
                    and compatible    (2/(n\_{`\text{in}`{=tex}}+n\_{`\text{out}`{=tex}}))   and fan-out
                    settings                                                                 

  He / Kaiming      ReLU-family       Variance (2/n\_{`\text{in}`{=tex}}) in a common form   Accounts for
                    activations                                                              ReLU's effect on
                                                                                             signal

  LeCun             SELU and related  Variance (1/n\_{`\text{in}`{=tex}}) in a common form   Used with
                    settings                                                                 appropriate
                                                                                             architectural and
                                                                                             training
                                                                                             assumptions
  ------------------------------------------------------------------------------------------------------------

These are common forms, not universal rules for every layer type.
Convolutional layers use fan-in and fan-out calculations that account
for kernel dimensions.

## 5. Bias Initialization

Biases are commonly initialized to zero in many feed-forward networks.
With properly initialized weights, zero biases do not force all neurons
to learn the same features.

Some architectures or specialized methods use other bias
initializations. Choose them based on the layer and model design rather
than assuming every parameter must use the same scheme.

## 6. Practical Example in PyTorch

PyTorch layers apply default initialization schemes, but you can
explicitly choose an initialization when the architecture calls for it.

``` python
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super().__init__()

        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

        # He/Kaiming initialization for ReLU hidden layer
        nn.init.kaiming_uniform_(
            self.fc1.weight,
            mode="fan_in",
            nonlinearity="relu",
        )
        nn.init.zeros_(self.fc1.bias)

        # Xavier/Glorot initialization for output layer
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.zeros_(self.fc2.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = MLP(input_dim=20, hidden_dim=64, output_dim=3)
print(model)
```

**Why these choices?**

-   The hidden layer uses ReLU, so Kaiming initialization is a common
    starting point.
-   Xavier is used for the output layer here as an illustrative choice;
    the best initialization depends on the output activation, loss, and
    architecture.
-   Biases are initialized to zero.

For an actual project, verify the framework's default initialization
before overriding it. Avoid reinitializing pretrained weights unless you
intentionally want to discard the learned parameters.

## 7. Choosing an Initialization

Use the following as a starting point, then validate on the actual
model:

-   **ReLU hidden layers:** start with He/Kaiming initialization.
-   **Tanh hidden layers:** start with Xavier/Glorot initialization.
-   **SELU networks:** consider LeCun normal and follow SELU's
    architectural requirements.
-   **Output layer:** choose based on the output activation, task, and
    loss; do not select an initializer solely from the layer's position.
-   **Pretrained models:** retain the pretrained initialization unless
    you have a specific reason to change it.

Initialization is one part of training stability. Also inspect input
scaling, normalization layers, learning rate, activation functions, and
gradient behavior.

## 8. Common Mistakes

-   Initializing every hidden-layer weight to zero.
-   Using a random distribution without considering its scale.
-   Treating variance and standard deviation as the same quantity.
-   Assuming one initializer is best for every activation and
    architecture.
-   Reinitializing pretrained model weights unintentionally.
-   Assuming good initialization alone prevents vanishing or exploding
    gradients.

## 9. Key Takeaways

-   Weight initialization sets trainable parameters before learning
    begins.
-   Random hidden-layer weights break symmetry; an appropriate scale
    helps maintain signal and gradient magnitudes.
-   Xavier/Glorot is commonly used for `tanh`-like settings.
-   He/Kaiming is commonly used for ReLU-family activations.
-   LeCun initialization is associated with SELU and its assumptions.
-   Biases can often start at zero.
-   Initialization helps training, but does not replace good data
    preprocessing, architecture choices, optimization, or validation.

## 10. Quick Self-Check

1.  Why can all-zero hidden-layer weights prevent neurons from learning
    different features?
2.  What is the main difference between Xavier and He initialization?
3.  In a normal distribution specification, what is the difference
    between variance and standard deviation?
4.  Why is initialization usually chosen with the activation function in
    mind?
5.  Why should pretrained weights not be reinitialized without a
    deliberate reason?

------------------------------------------------------------------------
